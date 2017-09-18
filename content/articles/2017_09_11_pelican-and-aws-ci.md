Title: Deploying a Static Webiste Using Cloudformation
Date: 2017-9-18 20:03
Modified: 2017-9-18 20:03
Category: meta, AWS, Cloudformation, S3 
Slug: pelican-and-aws-ci
Summary: First post! First in series of 'meta' posts describing the build, architecture, deployment and CI process for this website. [robarthur.co.uk](#) is built and deployed using AWS hosting tools, a python static site generator and AWS hosted CI pipeline.Simple Storage Solution (S3). ![Static Website Architecture - Cloudformation Template](images/static-website-s3-architecture-preview.png){.img-center}

## Overview

This first post covers the **hosting and deployment** for this website.  [robarthur.co.uk](#) is deployed as a static website to **Amazon Simple Storage Solution (S3)**.  S3  is a great solution for deploying static content, as all of the work to handled by Amazon.  The infrastructure to host the website itself is defined as code and deployed using AWS Cloudformation.

## Architecture

The setup is mostly as defined in the AWS S3 docuemntation for [hosting a static website with a custom domain](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)

![Static Website Architecture - Cloudformation Template](images/static-website-s3-architecture.png){.img-center}

Key services utilised are:

* S3 - For hosting and serving static content.  The three buckets hold 1) The static website content, 2) Manage redirects from the 'naked' domain to the 'www' domain, 3) Hold HTTP acces logs for the site
* Cloudfront - A CDN for handling globally distributed content, including edge level caching.
* Route53 - DNS provider for the website.
* Certificate Manager - Provision and manage SSL certificates
* Cloudformation - A template defines all of the above infrastructure as code.  Cloudformation provisions the infrastructure as defined in the template.

## Infrastructure as Code

A **Cloudformation template** defines all of the website infrastructure as code.  The template used to build the hosting infrastructure is defined here: 

## Future work TODO...

