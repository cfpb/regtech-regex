import { parse as yamlParse } from "yaml";
import * as fs from 'fs';
import * as path from "path";

const __dirname = path.dirname(path.resolve('./package.json'));
const content = fs.readFileSync(path.resolve('src/validations.yaml'), {encoding: "utf8"});
const configs = yamlParse(content);
fs.writeFileSync(path.join(__dirname, '/src/validations.json'), JSON.stringify(configs, null, "\t"));