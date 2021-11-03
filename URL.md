# URL Extraction


## Install

```bash
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install virtualenv python3 python3-dev python-dev gcc libpq-dev libssl-dev libffi-dev build-essentials
$ virtualenv -p /usr/bin/python3 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

# URL Feature Extractor
Extracting 111 features from URLs from your own database

### How to use
Run:

```bash
$ python run.py <input-urls> <output-dataset>
```
<input-urls> : Text files consisting of one or more url
<output-dataset> File format of choice (bytes, csv etc)

## Features implemented

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>LEXICAL</b>
        </th>
    </tr>
    <tr>
        <td>Count (.) in URL</td>
        <td>Count (-) in URL</td>
        <td>Count (_) in URL</td>
        <td>Count (/) in URL</td>
    </tr>
    <tr>
        <td>Count (?) in URL</td>
        <td>Count (=) in URL</td>
        <td>Count (@) in URL</td>
        <td>Count (&) in URL</td>
    </tr>
    <tr>
        <td>Count (!) in URL</td>
        <td>Count ( ) in URL</td>
        <td>Count (~) in URL</td>
        <td>Count (,) in URL</td>
    </tr>
    <tr>
        <td>Count (+) in URL</td>
        <td>Count (*) in URL</td>
        <td>Count (#) in URL</td>
        <td>Count ($) in URL</td>
    </tr>
    <tr>
        <td>Count (%) in URL</td>
        <td>URL LengthL</td>
        <td>TLD amount in URL</td>
        <td>Count (.) in Domain</td>
    </tr>
    <tr>
        <td>Count (-) in Domain</td>
        <td>Count (_) in Domain</td>
        <td>Count (/) in Domain</td>
        <td>Count (?) in Domain</td>
    </tr>
    <tr>
        <td>Count (=) in Domain</td>
        <td>Count (@) in Domain</td>
        <td>Count (&) in Domain</td>
        <td>Count (!) in Domain</td>
    </tr>
    <tr>
        <td>Count ( ) in Domain</td>
        <td>Count (~) in Domain</td>
        <td>Count (,) in Domain</td>
        <td>Count (+) in Domain</td>
    </tr>
    <tr>
        <td>Count (*) in Domain</td>
        <td>Count (#) in Domain</td>
        <td>Count ($) in Domain</td>
        <td>Count (%) in Domain</td>
    </tr>
    <tr>
        <td>Domain Length</td>
        <td>Quantidade de vogais in Domain</td>
        <td>URL domain in IP address format</td>
        <td>Domain contains the key words "server" or "client"</td>
    </tr>
    <tr>
        <td>Count (.) in Directory</td>
        <td>Count (-) in Directory</td>
        <td>Count (_) in Directory</td>
        <td>Count (/) in Directory</td>
    </tr>
    <tr>
        <td>Count (?) in Directory</td>
        <td>Count (=) in Directory</td>
        <td>Count (@) in Directory</td>
        <td>Count (&) in Directory</td>
    </tr>
    <tr>
        <td>Count (!) in Directory</td>
        <td>Count ( ) in Directory</td>
        <td>Count (~) in Directory</td>
        <td>Count (,) in Directory</td>
    </tr>
    <tr>
        <td>Count (+) in Directory</td>
        <td>Count (*) in Directory</td>
        <td>Count (#) in Directory</td>
        <td>Count ($) in Directory</td>
    </tr>
    <tr>
        <td>Count (%) in Directory</td>
        <td>Directory Length</td>
        <td>Count (.) in file</td>
        <td>Count (-) in file</td>
    </tr>
    <tr>
        <td>Count (_) in file</td>
        <td>Count (/) in file</td>
        <td>Count (?) in file</td>
        <td>Count (=) in file</td>
    </tr>
    <tr>
        <td>Count (@) in file</td>
        <td>Count (&) in file</td>
        <td>Count (!) in file</td>
        <td>Count ( ) in file</td>
    </tr>
    <tr>
        <td>Count (~) in file</td>
        <td>Count (,) in file</td>
        <td>Count (+) in file</td>
        <td>Count (*) in file</td>
    </tr>
    <tr>
        <td>Count (#) in file</td>
        <td>Count ($) in file</td>
        <td>Count (%) in file</td>
        <td>File length</td>
    </tr>
    <tr>
        <td>Count (.) in parameters</td>
        <td>Count (-) in parameters</td>
        <td>Count (_) in parameters</td>
        <td>Count (/) in parameters</td>
    </tr>
    <tr>
        <td>Count (?) in parameters</td>
        <td>Count (=) in parameters</td>
        <td>Count (@) in parameters</td>
        <td>Count (&) in parameters</td>
    </tr>
    <tr>
        <td>Count (!) in parameters</td>
        <td>Count ( ) in parameters</td>
        <td>Count (~) in parameters</td>
        <td>Count (,) in parameters</td>
    </tr>
    <tr>
        <td>Count (+) in parameters</td>
        <td>Count (*) in parameters</td>
        <td>Count (#) in parameters</td>
        <td>Count ($) in parameters</td>
    </tr>
    <tr>
        <td>Count (%) in parameters</td>
        <td>Length of parameters</td>
        <td>TLD presence in arguments</td>
        <td>Number of parameters</td>
    </tr>
    <tr>
        <td>Email present at URL</td>
    </tr>
</table>

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>HOST</b>
        </th>
    </tr>
    <tr>
        <td>Search time (response) domain (lookup)</td>
        <td>Domain has SPF?</td>
    </tr>
    <tr>
        <td>AS Number (or ASN)</td>
        <td>Time (in days) of domain activation</td>
        <td>Time (in days) of domain expiration</td>
    </tr>
    <tr>
        <td>Number of resolved IPs</td>
        <td>Number of resolved name servers (NameServers - NS)</td>
        <td>Number of MX Servers</td>
        <td>Time-to-live (TTL) value associated with hostname</td>
    </tr>
</table>

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>OTHERS</b>
        </th>
    </tr>
    <tr>
        <td>Valid TLS / SSL Certificate</td>
        <td>Number of redirects</td>
        <td>Check if URL is indexed on Google</td>
        <td>Check if domain is indexed on Google</td>
    </tr>
    <tr>
        <td>Uses URL shortener service</td>
    </tr>
</table>

