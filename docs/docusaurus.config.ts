import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Block Wrangler',
  tagline: 'Helping Minecraft shaderpack developers manage block IDs',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://github.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/block_wrangler/',
  trailingSlash: true,

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'camplowell', // Usually your GitHub org/user name.
  projectName: 'block_wrangler', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  plugins: [require.resolve('docusaurus-lunr-search')],

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Block Wrangler',
      logo: {
        alt: 'Block Wrangler Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/camplowell/block_wrangler',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Quickstart',
              to: '/docs/quickstart',
            },
            {
              label: 'Tag Library',
              to: '/docs/library/tags',
            }
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/me4JeAZ2Bf',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/camplowell/block_wrangler',
            },
          ],
        },
        {
          title: 'Other Resources',
          items: [
            {
              label: 'ShaderLABS',
              href: 'https://shaderlabs.org/wiki/Main_Page',
            },
            {
              label: 'Optifine Docs',
              href: 'https://github.com/sp614x/optifine/tree/master/OptiFineDoc/doc'
            },
            {
              label: 'Iris ShaderDoc',
              href: 'https://github.com/IrisShaders/ShaderDoc/tree/master'
            }
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Lowell Camp. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash']
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
