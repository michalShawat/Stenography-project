# XSS-attacks

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. 
XSS enables attackers to inject client-side scripts into web pages viewed by other users.

## Getting Started

Clone the project to your computer.

### Prerequisites

install webstorm .

### Installing

Install nodejs and express .

## Running 

Run the project and choose an attack .
run the attacks with the following scripts:

### Persistent XSS
```
<button onmouseover="alert(123)">hi</button>

<b onmouseover=alert('Wufff!')>click me!</b>
```
### Reflected XSS 
write this script as a user name in the URL.
```
<div><button onmouseover="alert(123)">hi</button></div>
```
### DOM XSS
write this after your name in the URL
```
<script>alert("You shouldn't click on unknown links!")</script>
 ```
 
 ## Authors

* **Galit Vaknin** - [Galit1321](https://github.com/Galit1321)

* **Ifat Neumann** - [neumani1](https://github.com/neumani1)

* **Michal Shawat** - [michalShawat](https://github.com/michalShawat)

## Acknowledgments

* The BIU Center for Research in Applied Cryptography and Cyber Security in Bar-Ilan University
