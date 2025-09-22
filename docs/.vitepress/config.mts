import {DefaultTheme, defineConfig} from 'vitepress'
import {groupIconMdPlugin, groupIconVitePlugin} from "vitepress-plugin-group-icons";
import {MermaidMarkdown, MermaidPlugin, withMermaid} from "vitepress-plugin-mermaid";

export default defineConfig({
    title: "SCH-Lib 文档",
    description: "sch lib 文档",
    lang: 'zh-CN',
    lastUpdated: true,
    ignoreDeadLinks: true,
    markdown: {
        lineNumbers: true,
        config: (md) => {
            md.use(MermaidMarkdown)
            md.use(groupIconMdPlugin)
            md.renderer.rules.heading_close = (tokens, idx, options, env, slf) => {
                let htmlResult = slf.renderToken(tokens, idx, options);
                if (tokens[idx].tag === 'h1') htmlResult += `<ArticleMetadata />`;
                return htmlResult;
            }
        }
    },
    vite: {
        plugins: [
            groupIconVitePlugin(),
            MermaidPlugin()
        ],
        optimizeDeps: {
            include: ['mermaid'],
        },
        ssr: {
            noExternal: ['mermaid']
        }
    },
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            {text: '教程', link: '/guide/introduction/', activeMatch: '^/guide/'},
        ],
        lastUpdated: {
            text: '上次更新'
        },
        editLink: {
            pattern: 'https://github.com/schlibra/sch-lib/edit/master/docs/:path',
            text: '在 GitHub 上编辑此页'
        },
        docFooter: {
            prev: '上一篇',
            next: '下一篇'
        },
        returnToTopLabel: '返回顶部',
        search: {
            provider: 'local',
            options: {
                translations: {
                    button: {
                        buttonText: "搜索文档"
                    }
                }
            }
        },
        outline: {
            label: '页面导航',
            level: 'deep'
        },
        sidebar: [
            {
                text: '简介',
                items: [
                    {text: '介绍', link: '/guide/introduction/'},
                    {text: '安装', link: '/guide/installation/'},
                    {text: '快速开始', link: '/guide/quickstart/'},
                ]
            },
            {
                text: '配置文件',
                items: [
                    {text: '配置文件加载类', link: '/guide/config/loader/'},
                    {text: '配置文件转换类', link: '/guide/config/convert/'}
                ]
            },
            {
                text: '日志处理',
                items: [
                    {text: '日志处理对象', link: '/guide/logger/logger/'},
                    {text: '日志配置', link: '/guide/logger/config/'}
                ]
            },
            {
                text: '头像生成',
                items: [
                    {text: '头像生成器', link: '/guide/avatar/'}
                ]
            },
            {
                text: 'MySQL',
                items: [
                    {text: 'MySQL对象', link: '/guide/mysql/mysql/'},
                    {text: 'MySQL表对象', link: '/guide/mysql/table/'}
                ]
            },
            {
                text: '实用工具',
                items: [
                    {text: 'Base64转换', link: '/guide/utils/base64/'},
                    {text: '剪切板操作', link: '/guide/utils/clip/'},
                    {text: 'Markdown转换', link: '/guide/utils/markdown/'},
                    {text: '密码隐藏', link: '/guide/utils/password/'},
                    {text: '二维码生成', link: '/guide/utils/qrcode/'},
                    {text: 'Mermaid', link: '/guide/utils/mermaid/'}
                ]
            },
            {
                text: '对象存储',
                items: [
                    {text: 'S3', link: '/guide/s3/'}
                ]
            }
        ],

        socialLinks: [
            {icon: 'github', link: 'https://github.com/schlibra'}
        ],

        lightModeSwitchTitle: '切换到暗黑模式',
        darkModeSwitchTitle: '切换到明亮模式',
    }

})


// https://vitepress.dev/reference/site-config

