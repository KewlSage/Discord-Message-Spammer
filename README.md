# Discord-Message-Spammer
**Description**

This will allow you to send messages using an account token, with a batch file that allows this to be use for for things like automatic server bumping or bot farming.

**WARNING**

THIS IS SELF BOTTING, I AM NOT RESPONSIBLE FOR ANY ISSUES YOU MAY COME IN TO DUE TO THIS FACT. USE AT YOUR OWN RISK.

**Usage (line 2 in the batch file)**
```
$ py <PATH OF PYTHON FILE> <TOKEN> <CHANNEL ID> "<MESSAGE>"
```

**Example**
```
file location: C:\Users\kronk\desktop\message spam.py

token: "msetdfhbae.etadh.xhrstgdsth"
channel id: 42069
message: !d bump
repeat after: 2 hours and 5 seconds
```

given that information, the batch file would look like this.

```bat
:za warudo
py C:\Users\kronk\desktop\message spam.py msetdfhbae.etadh.xhrstgdsth 42069 "!d bump"
timeout /t 7205
goto za warudo
```

that's about it.
