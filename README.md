# Mailing program

This program sends a newsletters to a specified list of clients

---

/Configs - contains the folowing configuration files:
- source_config.json - contains the sender's email:

```
{
    "email_sender": "login_example@gmail.com"
}
```

  _* it can be different email domains, not only @gmail.com_

- secret_config.json - contains the sender's email __password__:

```
{
    "email_password": "password_example"
}
```

- clients.json - contains the clients email list:
  
```
{
    "clients_list": [
        "login_example@gmail.com",
        "login_example1@mail.ru"
    ]
}
```

### TODO: 
- to update message module (to add some additional logics)
- to build logging system