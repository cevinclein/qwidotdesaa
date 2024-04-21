**Table of Contents**

[TOC]

# Overview 
---

bwVisu is quite simple and intuitively designed to make launching apps on the cluster as user-friendly as possible. Once you have successfully logged into bwVisu, the first thing you see is the dashboard. The dashboard presents a selection of available apps that the user can launch.

In the navigation bar, the user has the following options:

`Files` &mdash; `Interactive Apps` &mdash; `All Apps` &mdash; `My Interactive Sessions`

- **Files:** Here, the user has access to their home directory. In a graphical user interface, files can be downloaded and uploaded, and new files and folders can be created.
- **Interactive apps:** This displays the apps that the user can run on the cluster, possibly across multiple nodes. These apps initiate an interactive session which the user can directly connect to and, depending on the app, receive a graphical interface.
- **All Apps**: This shows all available apps.
- **My Interactive Sessions**: At bwVisu, it is possible to start several interactive apps simultaneously. Here, one can view an overview of currently running interactive apps or even completed sessions. It is also possible to view the log for each session.
  
# Files
---

If you click on the file menu, you will get two options:

- Home Directory
- OOD Config

The most relevant is access to the Home Directory because that's where results and logs from the apps are stored. The user gets the following interface:

![bwVisu-files](bwVisu-Wiki/images/bwVisu_files.png){.responsive}

The user interface is largely self-explanatory. However, an important note is that one can only access corners and files if they have the appropriate rights.

# Interactive Apps
---

When the user starts an interactive app, they receive an interface to configure which resources the app should use on the cluster. It is important to note that the interface can differ per app because each app can have individual configuration options.

![bwVisu-rstudio](bwVisu-Wiki/images/bwVisu_rstudio.png){.responsive}

Launching an app can take some time depending on the requested resources and cluster utilization. Upon successful launch of the app, you should get the following interface to connect with the app:

![bwVisu-rstudio-run](bwVisu-Wiki/images/bwVisu_rstudio_run.png){.responsive}

- **Host:** Indicates on which nodes the application is running.
- **Time Remaining:** Each application is given a time limit, which can also be set in advance. In this example, the application is supposed to run for one hour.
- **Session ID:** This is a link that leads to the folder of the session. Among other things, application logs are displayed here, which can be viewed in the UI.

To terminate an application, you can click the delete button or end the application in the interactive session. If the app is terminated in the interactive session, the window no longer shows `Running` but `Completed`. With the `Delete` button, you end the session and also remove the list entry from `My Interactive Sessions`.

## All Apps
---

In this section on the nav-bar you can find an overview of all available apps. Here you can search for specific apps by name or sort them if desired.

# My Interactive Sessions
---

In this section, you will get an overview of all ongoing and completed applications that were launched on the cluster. As soon as one starts an interactive app, one is automatically redirected here. Even if you log out of bwVisu and log back in, you can still see the information and logs from the finished interactive apps here until you delete it.
