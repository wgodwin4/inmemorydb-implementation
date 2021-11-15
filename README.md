# inmemorydb-implementation
In-memory db like redis for fun.

## *Run Instructions*
1. Download python 3.10.0
    * https://www.python.org/downloads/release/python-3100/
2. Install and Setup
    * https://phoenixnap.com/kb/how-to-install-python-3-windows
3. Open a terminal/cmd prompt
    * type (excluding the single quotes) 'python <path to main.py including main.py>'
    * press enter to start
4. You can start entering operations now

## *Data Commands*
SET name value – Set the variable name to the value value. Neither variable names nor values will contain spaces.

GET name – Print out the value of the variable name, or NULL if that variable is not set. UNSET name – Unset the variable name, making it just like that variable was never set.

NUMEQUALTO value – Print out the number of variables that are currently set to value. If no variables equal that value, print 0.

END – Exit the program. Your program will always receive this as its last command. Commands will be fed to your program one at a time, with each command on its own line. Any output that your program generates should end with a newline character.


## *Transaction Commands*
BEGIN – Open a new transaction block. Transaction blocks can be nested; a BEGIN can be issued inside of an existing block.

ROLLBACK – Undo all of the commands issued in the most recent transaction block, and close the block. Print nothing if successful, or print NO TRANSACTION if no transaction is in progress.

COMMIT – Close all open transaction blocks, permanently applying the changes made in them. Print nothing if successful, or print NO TRANSACTION if no transaction is in progress.
