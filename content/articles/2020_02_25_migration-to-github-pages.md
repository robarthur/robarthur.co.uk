Title: Migrating Site from S3 to Github Pages
Date: 2020-2-24 21:03
Modified: 2020-2-24 21:03
Category: Dev		
Tags: meta, Github
Slug: migration-from-s3-cloudfront-route53-to-github-pages
Summary: I decided to move this site's hosting from S3 to Github Pages.  Why?  Why Not! ![Migrating from S3 to Github Pages](images/migrating-site-from-s3-to-github-pages.png){.img-center}

## Overview

I recently moved the hosting from S3/Cloudfront to Github pages.  Given this is just a static site, there wasn't too much more to this than copying some files and changing some DNS records in Route53

Why the change?

 - Cloudfront is pretty heavyweight for a relatively simple static site.
 - Github pages is **free!** and supports free certificates through [Let's Encrypt](https://github.blog/2018-05-01-github-pages-custom-domains-https/), even on a custom domain.
 - I wanted to play around with Github Actions and this seemed like a nice entrypoint to that.

## Changes to Hosting and DNS Records

So with that in mind I used the following guide to create a branch to push my static content to and enable my site:

https://help.github.com/en/github/working-with-github-pages/creating-a-github-pages-site

Once that was in place, I confimred it was accessible at the project address: https://robarthur.github.io/robarthur.co.uk/

Now onto updating DNS Records... I decided I wanted to redirect to my apex domain https://robarthur.co.uk e.g. accessing https://www.robarthur.co.uk will redirect to http://robarthur.co.uk.  We want to make sure this is a proper 301 redirect so we get indexed correctly on search engines!

To use a custom domain with Github Pages I added the following records:

|         Name        |  Type |                                      Value                                     |
|:-------------------:|:-----:|:------------------------------------------------------------------------------:|
| robarthur.co.uk     | A     | 185.199.109.153 <br> 185.199.108.153 <br> 185.199.110.153 <br> 185.199.111.153 |
| www.robarthur.co.uk | CNAME | robarthur.co.uk                                                                |
|                     |       |                                                                                |

## Deploying Code

This changes how code is being deployed.  Rather than generating and pushing static content to an S3 bucket, we can simply push this to the default `gh-pages` branch.  From the the root of the project we could run...

```
# Setup the environment
python3 -m venv env/
source env/bin/activate
pip install -r requirements.txt

# Make and publish the content
make html
ghp-import output -p
```

Not we're making use of the [ghp-import package](https://github.com/davisp/ghp-import).  It handles all of the commits/pushing of content, and wraps up some of the magic for creating CNAME files. 

And that's it!  Our new static content is deployed.

## What's next?

So the whole purpose of this was to get some hands on experience with Github Actions.  I think I'm in a better place for this now as all of our dependencies are Python based and our deployment is to Github.  My hope is given this a Github action acting on a Github repo the credential/secrets management will be more intuative than pushing to S3... watch this space!