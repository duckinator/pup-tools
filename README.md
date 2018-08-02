# pup-tools

A collection of Python tools, available via `python3 -m pup.TOOL [...]`
or `pup.TOOL`, which provide built using only the Python standard library.

## Usage

### http

Fetch a document over HTTP.

```
$ pup.http get https://da.gd/ua
Python-urllib/3.6

$
```

### xpath

Run XPath queries on a document provided via stdin, and print the
results.

```
$ pup.http get 'http://rss.accuweather.com/rss/liveweather_rss.asp?locCode=02451' | pup.xpath ./channel/title ./channel/item/title
Waltham, MA - AccuWeather.com Forecast
Currently: Intermittent Clouds: 93F
$
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/duckinator/pup-tools. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The program is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the pup-tools project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/duckinator/pup-tools/blob/master/CODE_OF_CONDUCT.md).
