# web-recon
Wordlists, definitions, and validation regexes for the lazy hacker. web-recon aims to provide clear, reliable cheatsheets for files that shouldn't be published to public webservers, such as `.git` directories, backend packaging information, and more.

## Bishop
If you want to passively scan a subset of the websites you visit (which you are authorized to perform security testing against; such as penetration testing engagements) for exposed, problematic information, you can use the fantastically straightforward [bishop](https://github.com/jkingsman/bishop) extension from [Jack Kingsman](http://jacksbrain.com). All you need to do is install his Chrome extension, and either load in his predefined demos or one of the lists from our `bishop/` directory. The `bishop/verion_control.json` list is recommended, as it's minimally intrusive but most-critical.

# Wordlists
If you are looking to load these wordlists into your preferred spider, directory buster, etc., you'll probably want something out of the `wordlists/` directory. If there's anything in particular you're looking for - such as version control information that shouldn't be exposed - try wordlists like `wordlists/version_control.txt`.

## Development
Interested in contributing some nastygrams that you've seen people leave around or accidentally `rsync`'d to a server? We've got two 

### Structure
We keep things neat and tidy. In light of how disorganized wordlists and other shotgunned recon "intelligence feeds" can be, let's keep this as minimally spaghetti as possible. Each file to check is defined in YAML, has a few descriptive attributes, and is organized into folders by type (ex. package managers, version control, unconfigured applications). This has a number of benefits:

- You immediately know what has been found and why it is a finding.
- For tools that support it, you also get validation beyond "Wow, a 200! Time to throw an alert!"
- My life is 0.02% less frustrating to maintain.

### Contributing
Contributing is straightforward: create or append data to a YAML-formatted file in the most relevant `sources/<class_name>` folder, creating a new class name if none are relevant. Ensure it is named the path you want checked, and has a title, description for the finding, and validation regex. Then just run `compile.py`, add all the changed files, and submit an MR. Easy!

## License

This project is made available under the GPLv3. We kindly ask that if thie project has proved useful and you augment it with additional information, intelligence, etc. you make your changes available by PR to this repository.

Thanks! <3