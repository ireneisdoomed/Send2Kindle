<img src=https://github.com/ireneisdoomed/Send2Kindle/blob/master/images/thumbnail.jpg alt="200" width="850"/>

# Send2Kindle

Send2Kindle is a small application to automate the process of uploading an ebook to your Kindle.

This tool takes advantage of the function of [sending documents to your Kindle](https://www.amazon.com/-/es/gp/sendtokindle/email) as an email attachment provided by Amazon.

You can see a good description of how it works in this [Youtube video](https://www.youtube.com/watch?v=bkfoBYNJjIw) (in Spanish).

## Installation 🔧
Clone this repo to your local machine using:

```bash
git clone https://github.com/ireneisdoomed/Send2Kindle.git
```

## Pre-requisites 📐
Documents can only be sent to your Kindle devices or apps from e-mail accounts that you added to your Approved Personal Document E-mail List. 
To add an e-mail account, visit the Personal Document Settings page at Manage Your Kindle [here](https://www.amazon.es/mn/dcw/myx.html/ref=kinw_myk_redirect#/home/settings/payment).

Simply go to Preferences > Approved Personal Document E-mail List and add sendtokindle.py@gmail.com to set it up (no spam 😊).


## Usage 📦
It is currently necessary to run this script from the working directory.

If you are a Mac user:

```bash
python send2kindle.py file_path your_account@kindle.com
```

If you are a Linux user:

```bash
python send2kindle.py file_path your_account@kindle.com
```

## Contributing 👯
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
