import regexs from '@/validations.json';

export type RegtechRegexNames = "email" | "lei" | "rssd_id" | "simple_us_phone_number" | "tin";

export type RegtechRegexConfigs = Record<RegtechRegexNames, RegtechRegexConfig>;

export type RegtechRegexConfig = {
    description: string;
    error_text: string;
    regex: string;
    examples?: string[];
    link?: string;
    references?: string[];
};

export const RegtechRegex: RegtechRegexConfigs = regexs as RegtechRegexConfigs;

export default regexs as RegtechRegexConfigs;
