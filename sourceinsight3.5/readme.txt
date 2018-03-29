Source Insight 3.5 Readme File
Copyright (c) 1995-2003 by Source Dynamics, Inc.
Email: insight@sourceinsight.com
Web: http://www.sourceinsight.com

This file contains installation information and last minute information that 
was not able to be included in the User Manual. 

Contents
--------
1. Web Site
2. Trial Version
3. Installation
4. Compatibility With Old Versions
5. Windows NT/2000 Setup
6. Dual-Boot Systems
7. Performance Issues
--------


1. WEB SITE

Please visit our web site at http://www.sourceinsight.com for the latest product 
information, pricing, and maintenance releases.


2. TRIAL VERSION 

The Source Insight Trial Version is a fully functional version which will 
run for approximately 30 days.  We welcome you to use the trial version to see 
how well Source Insight works for you.  You can get the trial version at our 
web site: http://www.sourceinsight.com.  If you purchase a license, you will 
receive a serial number that unlocks and removes the trial period limitation.


3. INSTALLATION

Please refer to the Quick Start sheet included with the User Manual for 
setup instructions.   You will need the SERIAL NUMBER from the CD jacket
when you install Source Insight.  If you are using the Trial version, 
you can leave the serial number box blank and click the TRY button.

Please send in your registration card so that we can keep you informed of 
new developments.


4. COMPATIBILITY WITH OLD VERSIONS

You can use both version 3.5 and version 2.1 together on the same machine.  
They each use separate registry settings and should not conflict.  However 
you should follow these guidelines:

1. Install version 3.5 into a DIFFERENT directory than version 2.1.
2. Don't run instances of v. 2.1 and v. 3.5 at the same time.
3. Creating separate projects for version 3.5 is recommended, although the 
   project files are somewhat upward and downward compatible.  
4. You can open a version 2.1 project, but you will have to click the Browse 
   button in the Open Project dialog box to locate the old .PR file yourself.  
   If you installed v. 3.5 in a new directory (recommended), then v. 3.5 will 
   have no foreknowledge of the old projects already created.


5. WINDOWS NT/2000/XP SETUP

If you are installing on Windows NT/2000/XP, run the setup program from any user
that has permissions to install software and modify the HKEY_LOCAL_MACHINE 
registry hive. You do not need to have full Administration permissions to install 
Source Insight. The default NT "Power User" type will work fine.

Once installed Source Insight will appear in the "All Users" program group. 
Any user may access and run the program after it is installed.

User Data Directories: Due to the installation scheme described above, SI 
now creates folders within the SI program folder for each logged in user 
that runs SI.  For example, if John Smith was logged in and ran SI, and SI 
was stored in c:\Program Files\Insight3, then the following user data 
directory is created: c:\Program Files\Insight3\John Smith.  The user data 
directory contains configuration file (preferences settings) for the user.
It also contains the workspace file for the "no project open" mode.


6. DUAL-BOOT SYSTEMS

If you have a dual-boot system, you will have to install Source Insight 
separately under each OS.  However, you should install Source Insight into 
the same location on your disk.

If you are installing a maintenance release, please refer to the changes.txt 
file to read about changes and new features.


7. PERFORMANCE ISSUES

There are several options in Source Insight that can affect performance.  
Please see "Performance Tuning" in the User Manual or online help.




