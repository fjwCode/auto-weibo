# Publish plain text weibo automatically

```python
from utils import login_weibo, post_weibo


word = '#Cerium# This project is mainly targeted to users that need to \
communicate with Android devices in an automated fashion, such as in \
automated testing. https://github.com/fjwCode/cerium'

ACCOUNT = 'your account'
PASSWORD = 'your password'

chrome = login_weibo(ACCOUNT, PASSWORD)
post_weibo(chrome, word)
chrome.quit()
```