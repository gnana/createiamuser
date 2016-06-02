## Usage

usage: createiamuser.py [-h] --username USERNAME [--role ROLE]
                        [--password-only] [--accesskey-only]

## Example

createiamuser.py --username user1

createiamuser.py --username user1 --accesskey-only

createiamuser.py --username user1 --password-only

createiamuser.py --username user1 --role developer

createiamuser.py --username user1,user2,user3 --role developer
