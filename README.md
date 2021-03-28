# TrialShuffler

**Setup a new M5stack**

1. Download the following files:
  a.	M5 Burner
  b.	M5 Flow
  c.	Driver
  > You can find them in here (28.03.2021): https://m5stack-store.myshopify.com/pages/download
  > You only need to install the driver. The other two are zip files that you have to extract. The app is inside the zip files. 
  
2.	Copy the new files to the location you want to have them (eg. C:\ProgramFiles)	

3.	Connect the M5Stack to a USB port

4.	Open M5Burner
  a.	Choose the COM (~ USB connection)
  b.	Choose the device type on the left panel
  c.	Choose the version of the device you have (eg. UIFLOW(CORE2))
  d.	Click Burn
  e.	Click Start
    *NOTE: You don’t need to complete any of the fields.
  f.	Close M5Burner

5.	On the M5Burner select “UIFlow”
  a.	Select the mode to “USB”

>You have just finished the setup of your new M5Stack.
>More info on steps to setup your M5Stack: https://docs.m5stack.com/#/en/quick_start/m5core/m5stack_core_get_started_MicroPython
>Documentation on UIFlow MicroPython API: https://docs.m5stack.com/#/en/mpy/mpy_api_list // Select “M5Stack LVGL”


**Connect M5stack to Visual Studio Code**

1. Download git: https://git-scm.com/downloads

2. Download Visual Studio Code (VSC): https://code.visualstudio.com/download

3. Open VSC
  a. Click on "Extensions" on the left column
      > Install "Python"
      > Install "vscode-m5stack-mpy"
  b. Open the project you want to use on your M5stack
  c. Click on "Add M5Stack" on the bottom of the screen.
  d. Select the COM
