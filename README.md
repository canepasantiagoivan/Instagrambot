## **Bot de Instagram con Python**

![Diseño sin título](https://github.com/santiagocanepa/Optimizing-the-Management-of-1800-Own-Leads-in-HubSpot-Applying-XGB-CatBoost-and-Random-Forest/blob/dd7aaa56ebb62009f79d444f785590f41831d76a/imag/pngwing.com%20(4).png)



Welcome to this repository, where you will find scripts to automate some tasks on Instagram using Python and Selenium.

# 📋 Repository Contents
**create_unfollowers_list.py:** This script is responsible for scrolling and comparing lists of followers, creating a list called unfollowers.csv that contains those users who have stopped following us.

**stop_following.py:** This script stops following the users found in the unfollowers.csv list and adds these users to the add.csv list.

**follow_bot.py:** This script segments users by gender and sends follow requests to all users from another user's follower list, a followed list, or a likes list to ensure activity. Each user who is sent a request is copied into add.csv to avoid sending two requests to the same user.

**follow_bot_without_gender.py:** This script is an update of the previous script that removes the gender segmentation model so as not to load it if it is not going to be used.

# 📚 Pre-requisites
To use these scripts, you need to have the following Python packages installed:

selenium pandas beautifulsoup4 pickle random csv datetime

In addition, you will need the Chrome WebDriver, which you can download from here.

💻 How to use the scripts

Clone this repository locally.

bash git clone https://github.com/username/instagram-bot
**Update the username and password variables with your Instagram username and password in each script.**

username = 'enter username' # Change this to your Instagram username

password = 'enter password' # Change this to your Instagram password

Update the driver_path variable with the path to the Chrome WebDriver.
driver_path = 'path/to/chromedriver.exe' # Change this to the path to the Chrome WebDriver

Run the scripts in the order you wish using Python.

**python create_unfollowers_list.py 
python stop_following.py 
python follow_bot.py 
python follow_bot_without_gender.py**


# ❗ Important Note
Please note that using these scripts abusively can result in Instagram blocking your account. It is recommended to use them responsibly. This code is provided for educational purposes and spam or abuse on Instagram is neither encouraged nor supported.

# 🎯 Contribute
If you have any improvements or corrections, feel free to make a pull request. Make sure to test the code before submitting it.

# 📜 License
This project is under the MIT license.
