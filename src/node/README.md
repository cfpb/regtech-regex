# regtech_regex

Node project to provide a reusable node module to other node projects dependent on these regex's for validation of data.

## Installation

Until we start publishing to npm, install this github repo:

```
yarn add cfpb/design-system-react
```

If you're using yarn v2 or greater, [`yarn pack`](https://yarnpkg.com/advanced/lifecycle-scripts) will automatically build the package for you after it's installed.

## Usage

```ts
import type { RegtechRegexConfigs } from 'regtech-regex';
import validations from 'regtech-regex';

console.log(validations as RegtechRegexConfigs);

```

## Development

To persist changes made to validations.yaml:

1. Install Node v22+.
1. Enable [corepack](https://yarnpkg.com/getting-started/install): `corepack enable`.
1. `yarn`
1. `yarn build`

Note: This project uses yarn v3.5 in "plug n play" mode. There is no `node_modules/` directory. Packages are stored in `.yarn/cache/`.

## Open source licensing info

1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)
