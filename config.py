from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["TWITTER"] = {
    
    'consumer_key': "fktGsm2e6VfvCUZNflgwCnyOk",
    'consumer_secret': "vD2cBuXWN6fm4mdpDJepdDfoVGI0JEqmTlJT1tXAmISWJm8rrr",
    'access_token': "3104698248-t27PxxE2sAsV81NH45hiVhynNrB1rZaLau6eJdl",
    'access_token_secret': "8LdCL8LUbtCzszNmmzhndZpN7k1YkXbyupKLfvIy10YHy"
}


#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)