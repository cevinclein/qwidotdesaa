**Table of Contents**

[TOC]

# Intro 
---

![bw_concept](bwVisu-Wiki/images/bwVisu_concept.svg){.responsive}

When large quantities of scientific data is created (for example, from simulations), it is often necessary to employ hardware for further processing that is just as powerful as e.g. the HPC cluster that created the data in the first place. Transferring the data to a local workstation for visualization and analysis is typically not only time-consuming because of the data transfer itself, but the workstation may be ill-equipped to handle the workload. For such scenarios, remote solutions are needed, that employ powerful hardware and bring the applications to the data - and not vice versa.

The bwVisu project provides such a remote service for scientists from Baden-Württemberg as well as the corresponding software stack to deploy such a service on-premise. In bwVisu, the user can log in to an intuitive web frontend which manages interactive jobs running on an HPC cluster. Once a job has been started, the user can connect to it such that the application appears in a browser window with full 3D hardware acceleration provided by the cluster. The only requirement on the client side is that the browser must support HTML5.

# Getting started with bwVisu
---

**In order to get started with bwVisu, please proceed as follows:**

* In order to use bwVisu, it is required to be a user of the [bwForCluster Helix](https://wiki.bwhpc.de/e/Registration/bwForCluster) or a user of [SDS@hd](https://wiki.bwhpc.de/e/SDS@hd/Registration).
* Register for the service bwVisu at http://bwservices.uni-heidelberg.de. It is required to set a service password. Once a service password is set, use this password for the bwVisu login later on. It is also mandatory to register a token for two factor authentication at the bwservices site. More information about registering a token can be found [here](https://wiki.bwhpc.de/e/Registration/2FA).
* Once your registration has been completed, the bwVisu system will set up your user account. This can take up to 10 minutes, so please wait for around ten minutes before proceeding.
* Log in to the bwVisu web frontend at https://bwvisu-web.urz.uni-heidelberg.de. Your username will be `<site-prefix>_<uni-id>`, e.g. `hd_ab123` for a user from Heidelberg. The password will be your bwVisu service password set at `bwservices.uni-heidelberg.de`, and your registered device will be used as second factor.

## Open Ondemand
---

bwVisu is based on [Open Ondemand](https://openondemand.org) an open-source software platform designed to provide easy and streamlined access to high-performance computing (HPC) resources. Developed by the Ohio Supercomputer Center, it allows users to access HPC resources via a standard web browser, eliminating the need for a traditional command line interface.

The platform provides a range of tools and features, including:

1. **Web-based Access:** Users can manage jobs, files, and data directly through their browser.
2. **Interactive Applications:** It supports GUI-based applications like MATLAB, Jupyter Notebooks, and RStudio, enabling interactive computing and visualization.
3. **Job Management:** Users can easily submit, monitor, and manage their computing jobs on HPC resources.
4. **File Management:** Provides a file browser that allows users to upload and manage their data files without needing to use command-line FTP or SCP tools.

Open OnDemand aims to democratize access to supercomputing by making it more approachable and manageable for researchers, educators, and students.

# About
---

bwVisu is developed by:

/// hstack

![unihd](bwVisu-Wiki/images/unihd.png){height="80" widht="150"}
![hlrs](bwVisu-Wiki/images/hlrs.png){height="80" widht="150"}
![kit](bwVisu-Wiki/images/kit.png){height="80" widht="150"}

///

# Acknowledgements
---

We gratefully acknowledge funding by: 

![mwk](bwVisu-Wiki/images/mwk.png){height="80" widht="150"}


## bwVisu Acknowledgement
---

When preparing a publication describing work that involved the usage of bwVisu, please ensure that you reference the bwVisu project. The following sample text is suggested as a starting point:

> The authors acknowledge support by the state 
> of Baden-Württemberg through bwVisu.

In addition, we kindly ask you to notify us of any reports, conference papers, journal articles, theses, posters, talks which contain results obtained with the help of bwVisu resources by sending an email to bwvisu-support@urz.uni-heidelberg.de stating (e.g. in BibTeX-format):

- author(s)
- title or booktitle
- journal, volume, pages or editors, address, publisher
- year.

Such recognition is important for acquiring funding for the next generation hardware, support services, and infrastructure.

The publications will be referenced on the bwVisu website.

# Impressum
---

- https://www.urz.uni-heidelberg.de/de/Impressum



