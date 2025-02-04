import { resolve } from 'node:path';
import { defineConfig } from 'vite';
import dts from 'vite-plugin-dts';
import tsConfigPaths from 'vite-tsconfig-paths';
import { name } from './package.json';

export default defineConfig(() => ({
  resolve: {
    alias: {
      '~': resolve(__dirname),
      '@': resolve(__dirname, "./src")
    }
  },
  plugins: [
    tsConfigPaths(),
    dts({
      insertTypesEntry: true
    }),
  ],
  build: {
    outDir: 'src/node/dist',
    lib: {
      entry: resolve('src', 'node', 'index.ts'),
      name,
      formats: ['es', 'cjs'],
      fileName: (format): string => `${name}.${format}.js`
    },
    esbuild: {
      minify: true
    }
  }
}));
