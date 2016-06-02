## Usage

usage: createiamuser.py [-h] --username USERNAME [--role ROLE]
                        [--password-only] [--accesskey-only]

## Example

python createiamuser.py --username user1

python createiamuser.py --username user1 --accesskey-only

python createiamuser.py --username user1 --password-only

python createiamuser.py --username user1 --role developer

python createiamuser.py --username user1,user2,user3 --role developer
