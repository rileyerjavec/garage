| Date              |          |
|:------------------|:---------|
| TODO | Assigned |
| TODO    | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# SECURITY SENSATION BITES BACK: SUPERLATIVELY SECURED GARAGES GALORE

**Reported by `The Reporter` on `TODO`**

(Muufo) - Following the severe and sudden surge of new renters to vacant properties in `term-world`, a new blight seems to be bearing down on the otherwise blissful 'burbs of our tidy town. Incredibly, every single renting resident of `term-world` does not have access to all of the real estate being paid for.

Some years back, the owner of these newly domesticated domiciles--yes, real estate mogul `The Landlord`--invested in top-notch `garage` security features like the `Keypad.py` to allow residents to secure their vehicles and other `garage`-worthy gear with simple four digit codes. Here at `TNN`, we've learned that due to an oversight in moving-out processes, none of the codes to those security features were obtained prior to the former tenants leaving; this has resulted in sweeping security setbacks for `The Landlord` and his many new tenants.

That's right, none of the new `term-world` inhabitants have access to their `garage` interiors. This confounded correspondent is curious to see what unfolds next for these terrifically unlucky tenants...

## Addenda from the Mayor

> Congratulations on moving into your new house, my citizens! I, the Mayor, have given you all a free Groomba™ unit to help clear out your workshops so that you -- my
> citizens -- can begin work on building our _new world_! Very exciting, yes.
>
> But, I'm not all that knowledgeable about these things. Two key points I remember from the manual which seem to be important facts: it can move 1 foot
> every five seconds and the unit itself is 1 foot by 1 foot.
>
> _However_, the manufacturer did send out a recall for the units saying that they didn't work. I, your Mayor, am _far_ too busy to attend
> to these things. You can probably fix it yourself.

## Overview

Not only do you have a `house`, but you also have a handy `garage` -- a place where you can complete some experimental devices using your `workshop`. Like with everything `term-world` (as the news above tells us) there's a catch: the garage has a keycode which no one wrote down, and no one remembers. We have to use a device to -- there's no way around it -- _break in_.

Once in, have a look around your `WIDTH` x `LENGTH` garage!

In this set of activities we cover:

* basic Python syntax (i.e. way of "speaking" python)
* performing simple calculations in Python using `operators`
* first steps toward reading and working with a Python program
* continued practice operating and acting within a programming environment

### `KeypadCracker.py`

This device, the `KeypadCracker.py` has two (2) parts to it which create the first two (2) and last two (2) digits to our garage code. This means that the garage code as four (4) digits. Correctly computing the digits will allow you into your garage. Instructions for how to correctly arrive at this number are in the file itself.

### `Keypad.py`

Once you believe you have the right number, you need to input it into the `Keypad.py`. To do so run the following in your terminal:

`python Keypad.py --keycode YOUR_CODE`

(Replace `YOUR_CODE` with the computed code.)

When the number is correct, the `workshop` will open to you.

### `RoboVac.py`

You'll notice that, when you enter the `workshop`, there's a lot of junk laying around. The Groomba™ will clean this up for you, though you'll need to, as written, fix it. There are two well-defined areas of the code to fix (they're marked with `TODO`s). Once these are fixed, you should be able to use the dimensions of your `garage` to clean the junk out.

## Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the `README` might be taken out.

## Accessing `garage` Content

This time around, we will `clone` our repositories. This is the way we'll interact with `git` and GitHub for the remainder of the semester. We can consider a `clone` as something that's part download, part direct link. It's a similar relationship between that of GitHub, `term-world`, and our `house`.

The process has two (2) major parts.

### GitHub

- On your GitHub assignment page (i.e. _this_ page) locate the green `Code` button
- Select the `SSH` link from options presented
- `Copy` or click the button at the far right of the textbox on that screen

![TW - Clone link diagram](https://user-images.githubusercontent.com/1552764/213940345-2e62ec2e-e017-40ff-b325-745f9e731041.png)

### `term-world`

![TW - Clone Repo](https://user-images.githubusercontent.com/1552764/213931807-993be051-59e4-4102-b183-8c65bacaadee.png)

- In `term-world`, find the `Source Control` menu
- Locate and click the `...` at the top right of the window
- Choose `Clone` from the list of options
- Paste the link copied above
- Choose your home folder as the location into which to clone the repository

## Evaluating `garage` Content

Just like last week, the content for this week (and most every week to follow) is outfitted with a `grader` program that can be used to evaluate your work for the week.

Again, in order to run the `grader` for this week's work, you'll need to be in the topmost level of the `garage` folder (the same place you needed to be in order to successfully run the `git pull` command).

Once there, run the command:

```
gatorgrade
```

The `grader` will take a few minutes to do its work, but once it's complete the program will populate your terminal window with a series of checks that gauge the overall "completeness" of your work. Be sure to have *all* of the checks completed by the due date!

### `push`ing Content

The GitHub platform is a place to store your work. So, it makes some sense that should be able to download from it, and push back (upload) to it. Here, we'll learn this second part.

Bottom line: we need to tell git that there have been changes.

Observe the list of files you've changed and add them to a staging area using the + button to the right of each file
Once these have been "staged," attach a message to what we call a commit -- a "packaging" of the files to send to GitHub.

To follow this process:

![TW - Commit and Sync](https://user-images.githubusercontent.com/1552764/213940290-23b12a8a-6283-492c-ab1c-66a801ba815e.png)

## `term-world` Server Backup Policy

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e., weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
