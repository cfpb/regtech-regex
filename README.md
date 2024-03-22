# regtech-regex

Shared data validations using regular expressions for use at the CFPB. This repo aims to collect sensible regex data validations in one YAML file for use across multiple tech stacks in the Small Business Lending project and maybe beyond.

This YAML file is subject to sudden and breaking changes while the Small Business Lending project is in development, so use at your own risk.

![A rough diagram of the regtech-regex vision of a single YAML file sharing the same regular expression for validating data such as Research, Statistics, Supervision, Discount IDs across multiple use cases. The diagram shows a YAML object that contains a RSSD ID number along with a regex that ensures that the value is an integer. Two arrows point from the YAML: one arrow points to a file that has an RSSD ID that is 9999 with a green validation check mark, and the other arrow points toward a file that has an RSSD ID with a red invalid symbol of X](regtech-regex.svg)

## Dependencies

This repo doesn't currently have any dependencies. Just a good old YAML file.

## Installation

Import the `validations.yaml` file using the URL or via a package manager.

## Usage

Here's an example of an entry in the `validations.yaml` file:

```yaml
rssd_id:
  description: must be an integer
  examples:
    - '9999'
    - '1'
  link: https://regex101.com/r/l3SyQi/3
  regex: ^\d+$
```

Each entry should be snake case, with common acronyms and initialisms being acceptable.

Each entry should have 4 properties: description, examples, link, and regex.

- description: short description of how this value should be validated
- examples: an array of strings that are examples of values that would be validated as being correct
- link: a link to [regex101.com](https://regex101.com/) for live documentation and so devs can easily test the regular expression
- regex: the regular expression that validates the value

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

Think you might have a simple regular expression that relates to consumer finance that might be helpful? Create an issue! See [CONTRIBUTING](CONTRIBUTING.md) for more details.

---

## Open source licensing info

1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

---

## Credits and references

1. Screenshot uses icons from the [CFPB Design System](https://cfpb.github.io/design-system/foundation/iconography) and composed with [tldraw](https://www.tldraw.com/)
