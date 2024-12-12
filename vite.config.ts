import eslintPlugin from '@nabla/vite-plugin-eslint';
import { resolve } from 'node:path';
import { defineConfig } from 'vite';
import dts from 'vite-plugin-dts';
import svgLoader from 'vite-svg-loader';
import tsConfigPaths from 'vite-tsconfig-paths';
import { name } from './package.json';

export default defineConfig(() => ({
  resolve: {
    alias: {
      '~': resolve(__dirname)
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