# suspicious-files
Short, relatively optimized wordlists of files and directories that should (rarely) be hosted on a webserver.

## Usage
If you are looking to load these wordlists into your preferred spider, directory buster, etc., you'll probably want something out of the `compiled/` directory. If there's anything in particular you're looking for - such as version control information that shouldn't be exposed - try wordlists like `compiled/version_control.txt`.

## Structure
We try to keep things neat and tidy, and group by directory. That way we know *immediately*:
- Why something has been added
- If found on a public server, what that particular find is relevant to

This of course prevents directory busting wordlist spaghetti, such as what happened to Dirb's included wordlists.

This also allows you to easily build your own lists by catting together whatever might be most relevant to you - maybe you know you're scanning a PHP site and want to look for PHP-related information and vulnerabilities. It's super straightforward to optimize your search: grab the PHP, Composer, and file traversal lists... don't bother looking for `cgi-bin`!

## License

This project is made available under the GPLv3. We kindly ask that if thie project has proved useful and you augment it with additional information, intelligence, etc. you make your changes available by PR to this repository.

Thanks! <3