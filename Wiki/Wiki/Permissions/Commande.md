
# Lesson One -- Never use C-shell f or SUID script s.

````bash
cat change-pass
#!/bin/ksh
user=$1
passwd $user
````

R ew riting the script in K orn shell helps us avoid the C-shell problem, but w e still have problems. The script is
vulnerable to a hacker manipulating the *PATH variable*. Because the program *uses relative path names*, a hacker can
change his PATH to use his ow n program instead of the regular /usr/bin/passwd program:

## Solution : 

````bash
export PATH='/tmp'
echo "cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755/tmp/sh" >/tmp/passwd
./change-pass
````

The PATH has been changed, and the change-pass command now runs the /tmp/passwd program instead of the /usr/bin
/passwd program that w e intended

# Lesson Two -- A lways manually set t he PATH and use absolut e pat h names.

````bash
cat change-pass
#!/bin/ksh
PATH='/bin:/usr/bin'
user=$1
/usr/bin/passwd $user
````

Now the PATH is secure and w e are using absolute paths; but look closely and see that this script can change any
passw ord, even root's! We don't w ant the help desk (or a hacker) using our script to change root's password.

# Lesson Three -- Underst and how t he programs in your script work.

````bash
% cat change-pass
#!/bin/ksh
PATH='/bin:/usr/bin'
user=$1
rm /tmp/.user
echo "$user" > /tmp/.user
isroot='/usr/bin/grep -c root /tmp/.user'
[ "$isroot" -gt 0 ] && echo "You Can't change root's password!" && exit
/usr/bin/passwd $user
````

Now this script w ill exit if someone enters root as the argument. But w hat happens if a hacker runs the program and
doesn't specify an argument? The program w ill run the passwd command w ithout any arguments. When the passwd
command doesn't receive any argum ents, it defaults to the current user. The problem is that in a root-ow ned SUID
script, the current user is alw ays root. The help desk (or hacker) can still change root's passw ord by not giving
change-pass any arguments

# Lesson Four -- Don't use t emporary f iles! If you must use t emporary f iles, don't put t hem in a publicly writ able area.

````bash
% cat change-pass
#!/bin/ksh
PATH='/bin:/usr/bin'
user=$1
[ -z $user ] && echo "Usage: change-pass username" && exit
[ "$user" = root ] && echo "You can't change root's password!" && exit
/usr/bin/passwd $user
````

There are no temporary files, but now a hacker can use the w ell-know n sem i-colon trick. A sem i-colon lets you put
more than one com mand on a single line. By taking advantage of this, a hacker could type:
*% change-pass "user;cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755 /tmp/sh*"
Our script w ould take this input and run:
*/usr/bin/passwd user;cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755 /tmp/sh*

````bash
% cat change-pass
#!/bin/ksh
PATH='/bin:/usr/bin'
user=${1##*[ \\$/;()|\>\<& ]}
[ -z $user ] && echo "Usage: change-pass username" && exit
[ "$user" = root ] && "You can't change root's password!" && exit
/usr/bin/passwd $user
````

# Lesson Five -- Dist rust and check all user input , and st rip out any met a-charact ers.

Another common vulnerability is related to a shell's Internal Field Separator (IFS). The IFS specifies w hich characters
separate commands. It is normally set to a space, tab, or new line. By changing the IFS, a hacker can change w hat
programs our script executes. Our script calls the /usr/bin/passwd program. Changing the IFS to "/" w ith
*% export IFS='/*

# Lesson Six -- A lways manually set your IFS.

````bash
% cat change-pass
#!/bin/ksh
PATH='/bin:/usr/bin'
IFS=' '
user=${1##*[ \\$/;()|\>\<& ]}
[ -z $user ] && echo "Usage: change-pass username" && exit
[ "$user" = root ] && "You can't change root's password!" && exit
/usr/bin/passwd $user
````

Unfortunately, w e are still not safe. There is an inherent race condition in shell scripts that w e can't fix w ith better
programming. The problem is that running a shell script is a tw o-step process. First, the system starts up a new shell.
Then, the new shell reads the contents of the script and executes it. By tim ing things perfectly, a hacker can exploit
the delay betw een shell startup and w hen the script is read and executed. By creating a link to the SUID script:

````bash
% cd /tmp
% ln -s change-pass rootme
````

running the link, and quickly replacing it w ith another file:

````bash
% ./rootme &
% rm rootme && \
echo "cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755 /tmp/sh" \
>> rootme
````

It is possible to run anything as root. Done like this, there is only a small chance the attack w ould succeed, but there
are techniques and programs to increase the chances of success and to automate the procedure for you. There are
only tw o defenses against this attack. First, do not use SUID shell scripts. Second, some system s (e.g., Solaris)
prevent this race condition by passing an open file handle to the new shell, thus avoiding the need to reopen and read
the SUID file.