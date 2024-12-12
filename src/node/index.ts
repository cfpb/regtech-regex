import { parse as yamlParse } from "yaml";
import * as fs from 'fs';
import * as path from "path";

export interface RegtechRegexConfigs extends Record<string, RegtechRegexConfig> {
}

export interface RegtechRegexConfig {
    description: string;
    error_text: string;
    regex: string;
    examples?: string[];
    link?: string;
    references?: string[];
}

export const getRegex = () => {
    const content = fs.readFileSync(path.resolve(__dirname, '/src/validations.yaml'), {encoding: "utf8"});
    const configs = yamlParse(content) as RegtechRegexConfigs;
    return configs;
}

export const RegtechRegex = getRegex();

export default RegtechRegex;