const e = {
  description: "must conform to common email conventions using the W3C method of email validation which is only a subset of full RFC 5322 compliance",
  error_text: "Must be a valid email address.",
  examples: [
    "a-test-email-account@cfpb.gov",
    "ASuperCoolEmailAccount@cfpb.gov"
  ],
  link: "https://regex101.com/r/bUsmeo/2",
  references: [
    "https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)"
  ],
  regex: "^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
}, t = {
  description: "must be 18 characters that only contain A-Z and 0-9 followed by 2 digits",
  error_text: "Must be a valid LEI of 20 characters that only contain A-Z and 0-9 (no special characters).",
  examples: [
    "123400TESTBANK000192",
    "123400TESTBANK000289",
    "123400TESTSUBBANK147",
    "123400TESTSUBBANK244",
    "TESTBANK123456789012"
  ],
  link: "https://regex101.com/r/ItOdOj/3",
  regex: "^[A-Z0-9]{18}\\d{2}$"
}, o = {
  description: "must be an integer",
  error_text: "Must be a number.",
  examples: [
    "9999",
    "1"
  ],
  link: "https://regex101.com/r/l3SyQi/3",
  regex: "^\\d+$"
}, i = {
  description: "must be a simple United States phone number pattern of 3 digits, followed by a hyphen, followed by 3 digits, followed by a hyphen, followed by 4 digits",
  error_text: "Must be a valid phone number in the format of 555-555-5555.",
  examples: [
    "555-555-5555",
    "555-123-4567"
  ],
  link: "https://regex101.com/r/jt6ujJ/5",
  regex: "^\\d{3}-\\d{3}-\\d{4}$"
}, s = {
  description: "must be 2 digits, followed by a hyphen, followed by 7 digits",
  error_text: "Must be a valid TIN in the format of 12-3456789.",
  examples: [
    "12-3456789",
    "98-7654321"
  ],
  link: "https://regex101.com/r/7op0LA/3",
  regex: "^\\d{2}-\\d{7}$"
}, a = {
  email: e,
  lei: t,
  rssd_id: o,
  simple_us_phone_number: i,
  tin: s
}, n = a;
export {
  n as RegtechRegex,
  n as default
};
