# Meme Generator

Simple application allowing to generate memes composing of one of the avialable image templates and up to two text boxes

## Table of contents
* [General info](#general-info)
* [Implementation ideas](#implementation-ideas)
* [Run](#run)
* [Technologies](#technologies)
* [Examples of program effects](#examples-of-program-effects)
* [Status](#status)

## General info

This program allows user to select one of the avilable meme templates and add up to two captions to it.

Application allows searching meme tempalte by name and selecting random template from all of the avilable (after filtering only filtered memes are taken into consideration when choosing random template).

Application allows also to save image created with it locally.

In order to be able to generate memes with this application one needs an account on [imgflip](https://imgflip.com/)

## Implementation ideas

My main goal was to create simple desktop app for creating memes. With that in mind I wanted to learn improve my skills with GUI in python and practice some of the popular design patterns in this language.

I used tkinter for UI and [imgflip](https://imgflip.com/) API in order to acquire meme templates and add text to them.

## Run

If you don't have, Tkinter or Pillow installed, use the command:
```bash
pip install tk pillow
```
To get started with my program, navigate to a directory where you want to use the project, then clone it with:
```bash
git clone https://github.com/WWykret/meme-generator.git
```
or
```bash
git clone git@github.com:WWykret/meme-generator.git
```
If you don't want to use git clone for whatever reason, you can manually download it, and move the folder somewhere convenient. Then, open up your terminal, and go to the correct directory. Then just run the program:
```bash
python3 main.py
```

## Technologies

The program was written in Python using Tkinter for creating GUI, [imgflip](https://imgflip.com/) for creating memes and Pillow for operations on images obtained from the API.

## Examples of program effects

#### Example. 1
![example1](https://github.com/WWykret/Webcam-Image-Transformer/blob/main/examples/example1.jpg)

#### Example. 2
![example2](https://github.com/WWykret/Webcam-Image-Transformer/blob/main/examples/example2.jpg)

#### Example. 3
![example3](https://github.com/WWykret/Webcam-Image-Transformer/blob/main/examples/example3.jpg)

#### Example. 4
![example4](https://github.com/WWykret/Webcam-Image-Transformer/blob/main/examples/example4.jpg)

## Status

I consider this project to be finisned and will probably not work on it anymore.