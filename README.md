# pup-tools

A collection of Python tools, available via `python3 -m pup.TOOL [...]`,
which provide nice tools built using the Python standard library.

## Usage

### xpath

Run XPath queries on a document provided via stdin, and print the
results.

```
$ curl -s 'http://rss.accuweather.com/rss/liveweather_rss.asp?locCode=02451' | python3 -m pup.xpath ./channel/title ./channel/item/title
Waltham, MA - AccuWeather.com Forecast
Currently: Intermittent Clouds: 93F
$
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/duckinator/pup-tools. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the pup-tools project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/duckinator/pup-tools/blob/master/CODE_OF_CONDUCT.md).
