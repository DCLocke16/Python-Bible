# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

username = email[:email.index("@")]

# slice out domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your user name is {} and your domain name is {}.".format(username, domain)

# display output message
print(output)
