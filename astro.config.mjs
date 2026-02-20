import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://techpulse-global.pages.dev',
  output: 'static',
  // CSSの崩れを防ぐための設定
  integrations: [], 
});
