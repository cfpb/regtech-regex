import { describe, it, expect } from 'vitest';
import { RegtechRegex, RegtechRegexNames } from '../index';

describe('RegtechRegex', () => {
  it('should have all expected regex configurations', () => {
    const expectedConfigs: RegtechRegexNames[] = [
      'email',
      'lei',
      'rssd_id',
      'simple_us_phone_number',
      'tin',
    ];

    expectedConfigs.forEach((configName) => {
      expect(RegtechRegex).toHaveProperty(configName);
      expect(RegtechRegex[configName]).toHaveProperty('regex');
      expect(RegtechRegex[configName]).toHaveProperty('description');
      expect(RegtechRegex[configName]).toHaveProperty('error_text');
    });
  });

  describe('email regex', () => {
    it('should match valid email addresses', () => {
      const goodEmail = 'Jason.Adam@cfpb.gov';
      const regex = new RegExp(RegtechRegex.email.regex);

      expect(regex.test(goodEmail)).toBe(true);
    });

    it('should not match invalid email addresses', () => {
      const badEmail = 'something@bad_domain';
      const regex = new RegExp(RegtechRegex.email.regex);

      expect(regex.test(badEmail)).toBe(false);
    });
  });

  describe('lei regex', () => {
    it('should match valid LEI codes', () => {
      const goodLei = '1234567890ABCDEFGH00';
      const regex = new RegExp(RegtechRegex.lei.regex);

      expect(regex.test(goodLei)).toBe(true);
    });

    it('should not match LEI codes that are too short', () => {
      const badLei = '123';
      const regex = new RegExp(RegtechRegex.lei.regex);

      expect(regex.test(badLei)).toBe(false);
    });

    it('should not match LEI codes that are too long', () => {
      const anotherBadLei = '1234567890ABCDEFGHIJ';
      const regex = new RegExp(RegtechRegex.lei.regex);

      expect(regex.test(anotherBadLei)).toBe(false);
    });
  });

  describe('rssd_id regex', () => {
    it('should match valid RSSD IDs', () => {
      const goodRssd = '1234';
      const regex = new RegExp(RegtechRegex.rssd_id.regex);

      expect(regex.test(goodRssd)).toBe(true);
    });

    it('should not match invalid RSSD IDs', () => {
      const badRssd = 'ABC';
      const regex = new RegExp(RegtechRegex.rssd_id.regex);

      expect(regex.test(badRssd)).toBe(false);
    });
  });

  describe('simple_us_phone_number regex', () => {
    it('should match valid phone numbers', () => {
      const goodPhone = '555-555-5555';
      const regex = new RegExp(RegtechRegex.simple_us_phone_number.regex);

      expect(regex.test(goodPhone)).toBe(true);
    });

    it('should not match invalid phone numbers', () => {
      const badPhone = '12-34-56-78-90';
      const regex = new RegExp(RegtechRegex.simple_us_phone_number.regex);

      expect(regex.test(badPhone)).toBe(false);
    });
  });

  describe('tin regex', () => {
    it('should match valid TIN numbers', () => {
      const goodTin = '98-7654321';
      const regex = new RegExp(RegtechRegex.tin.regex);

      expect(regex.test(goodTin)).toBe(true);
    });

    it('should not match invalid TIN numbers', () => {
      const badTin = '123456789';
      const regex = new RegExp(RegtechRegex.tin.regex);

      expect(regex.test(badTin)).toBe(false);
    });
  });
});
