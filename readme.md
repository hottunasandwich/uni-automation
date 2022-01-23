# Golestan

It's a robot for [Golestan](http://golestan.sbu.ac.ir) Automation with its website.

### Installation 

For installation you can simply clone it.

* ###### First step

Install Python on your machine you should know how ;)

* ###### Second step 

Install selenium package
`pip install selenium`
or
`py -m pip intall selenium`

* ###### Third step

Make sure `chromedriver.exe` matches your chrome version, mine was _79.0.3945.130 (Official Build) (64-bit)_

* ###### Fourth step

  - Replace your _username_ and _password_ with the one in `robot.py`
  - Replace your _units_ as a list in `robot.py` as mentioned
# How to run

Simply enter code below in your cmd opened in the same directory that you have cloned the project.
`py robot.py`
or 
`python robot.py`

# Tips 

While the App is running you have to pay attention to some precautions

  1. It doesn't have any Captcha Detector so you have to do it by yourself.
  2. In any Stage if it crashes just quit and start it over. 
  3. At the end you have to submit your Form it wouldn't do it for you (you have started it you have to finish it :)) )
