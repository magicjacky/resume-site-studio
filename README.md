# Resume Site Studio · 简历网站工坊

这是一个可单次安装的求职与简历网站主 Skill。它内置职位匹配证据分析器，可先分析招聘要求和真实经历，再把简历、履历或项目资料转换成可编辑的个人网站。核心是通用的 `SKILL.md`，没有平台专属命令、付费服务或外部依赖。`assets/starter/` 是可选的静态网站示例，包含专业和动态两种展示模式。示例里的“林序”及其履历均为虚构内容。

## 一键下载

**[下载最新版安装包：resume-site-studio-workbuddy.zip](https://github.com/magicjacky/resume-site-studio/releases/latest/download/resume-site-studio-workbuddy.zip)**

[查看全部版本与更新说明](https://github.com/magicjacky/resume-site-studio/releases)

下载的是 GitHub Release Asset，里面已经同时包含主 Skill 和 `job-fit-evidence-analyzer` 模块。仓库中的 `assets/starter/` 是简历网站演示素材，与 GitHub 的 Release Assets 不是同一个概念。

## 包含内容

- `SKILL.md`：跨平台工作流程与交付标准。
- `modules/job-fit-evidence-analyzer/`：内置的职位匹配、硬门槛和证据缺口分析 Skill。
- `references/`：事实提取、动态设计和验收清单。
- `assets/starter/`：无需构建即可预览的 HTML/CSS/JavaScript 示例。
- `agents/openai.yaml`：Codex 可选展示信息；其他平台可忽略。
- `scripts/package_workbuddy.py`：生成含 WorkBuddy 额外元数据的上传 ZIP，不改变通用版。
- `dist/resume-site-studio-workbuddy.zip`：已经生成的单次安装包，内含主 Skill 和职位分析模块。

## 安装

只需复制或导入整个 `resume-site-studio` 文件夹一次。主 `SKILL.md` 会根据任务自动读取内置模块，不需要再单独安装 `job-fit-evidence-analyzer`。不同平台的装载入口如下；具体产品版本可能调整入口位置。

| 平台 | 安装方式 |
| --- | --- |
| Codex | 复制到用户技能目录（本机可用 `~/.codex/skills/`；新版文档也列出 `~/.agents/skills/`）或项目的 `.agents/skills/`。 |
| Claude Code | 复制到 `~/.claude/skills/`，或项目的 `.claude/skills/`。 |
| WorkBuddy | 运行 `python scripts/package_workbuddy.py` 生成上传 ZIP，然后在 Skill Marketplace 的“添加 Skill / 创建 Skill”导入。ZIP 根目录直接包含 `SKILL.md`。 |
| 豆包工作 | 使用客户端“技能 · 连接器 · 伙伴”中的自定义技能入口导入 Skill 文件；本包仅使用通用 `SKILL.md` 和相对路径资源。具体版本的本地目录与上传格式需在客户端核对。 |
| 千问办公 | 复制到 `~/.qwenworkcn/skills/`，或在“扩展 → 技能 → 安装技能”上传 `SKILL.md` 和辅助文件。 |

可以直接下载上方的最新版 ZIP，用于支持 ZIP 导入的平台。仓库中的 `dist/resume-site-studio-workbuddy.zip` 是同一安装包的源码仓库副本。安装后只需要调用 `resume-site-studio`；主 Skill 会根据任务自动读取内置模块。

建议先在各平台用一句话测试触发：“用 resume-site-studio 根据我的简历做一个个人网站，先生成本地预览。”能否自动触发取决于平台的技能发现机制；也可以直接指定技能名。

## 预览示例

直接打开 `assets/starter/index.html`。动态模式使用 CSS 渐变色雾与滚动出现动画；右上角可切换至明亮、安静的专业模式。系统设置为“减少动态效果”时会停用主要动画。无需联网或安装依赖。

## 使用真实简历

提供简历和目标用途（求职、个人介绍、作品集或学术主页），并说明愿意公开的联系方式。让技能先生成本地网站，确认文字、隐私和视觉效果后再发布。技能不会凭空补写经历、成果或量化指标。

如果网站面向某个明确职位，主 Skill 会自动调用内置的 `job-fit-evidence-analyzer`，生成职位要求与个人证据的对应表，再选择首页重点。用户也可以只让主 Skill 输出职位匹配报告，不生成网站。

## 许可与来源

本仓库采用 PolyForm Noncommercial License 1.0.0。允许非商业使用、修改和分发；分发时需要保留许可证和 Required Notice。商业使用需要另行授权。设计与流程参考项目及许可说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
