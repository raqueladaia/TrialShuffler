# TrialShuffler

**Setup a new M5stack**

1. Download the following files:
  1.	M5 Burner
  2.	M5 Flow
  3.	Driver
  > You can find them in here (28.03.2021): https://m5stack-store.myshopify.com/pages/download
  > You only need to install the driver. The other two are zip files that you have to extract. The app is inside the zip files. 
  
2.	Copy the new files to the location you want to have them (eg. C:\ProgramFiles)	

3.	Connect the M5Stack to a USB port

4.	Open M5Burner
  1. Choose the COM (~ USB connection)
  2. Choose the device type on the left panel
  3. Choose the version of the device you have (eg. UIFLOW(CORE2))
  4. Click Burn
  5. Click Start (*NOTE: You don’t need to complete any of the fields.*)
  6. Close M5Burner

5.	On the M5Burner select “UIFlow”
  1.	Select the mode to “USB”
  
You have just finished the setup of your new M5Stack.

>More info on steps to setup your M5Stack: https://docs.m5stack.com/#/en/quick_start/m5core/m5stack_core_get_started_MicroPython
>Documentation on UIFlow MicroPython API: https://docs.m5stack.com/#/en/mpy/mpy_api_list // Select “M5Stack LVGL”


**Connect M5stack to Visual Studio Code**

1. Download git: https://git-scm.com/downloads

2. Download Visual Studio Code (VSC): https://code.visualstudio.com/download

3. Open VSC
  1. Click on "Extensions" on the left column
      1. Install "Python"
      2. Install "vscode-m5stack-mpy"
  2. Open the project you want to use on your M5stack
  3. Click on "Add M5Stack" on the bottom of the screen.
  4. Select the COM
