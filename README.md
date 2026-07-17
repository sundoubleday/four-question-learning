# 学会如何学习 · Skills

> 把"听过、读过、收藏过却用不起来"的知识，真正变成你能用的东西。一套以**四问学习法**为主框架的中文 AI Skills。

**支持：WorkBuddy、豆包、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

本仓库从刘澜《学会如何学习：120堂认知升级课》(机械工业出版社, 2025) 蒸馏而来：通读全书后提炼出 271 条候选（框架/原则/案例/反例/术语），经三重验证归并为 **8 个可直接调用的 Skills**，并通过 48/48 盲测。

[快速开始](#快速开始) · [安装](#安装) · [能力一览](#能力一览) · [精华长文 DIGEST](docs/DIGEST.md) · [索引 INDEX](docs/INDEX.md)

---

## 这套 skill 解决什么问题

你不需要先背下这 8 个工具叫什么。**照常说人话**，对应的 skill 会自己冒出来。

| 你真实的处境 | 自动触发 |
|---|---|
| "我刚听完一本书 / 一节课，不知道怎么用起来" | `si-wen-xuexi-fa` 四问学习法（主框架） |
| "这个问题老是反复出现，找不到根本原因" | `faxian-moshi` 发现模式 |
| "这个新领域我到底该学什么、学到什么程度" | `moshi-jujiao-xuexi` 模式化学习 |
| "我学了半天，说不清自己到底学到没有" | `xuexi-tiwen` 学习有体温 |
| "感觉一直在被动听课，怎么才算真学进去" | `xuexi-fangshi-dengji` 学习方式等级 |
| "老师/书给的答案，我该照单全收还是怀疑" | `cankao-daan-siwei` 参考答案思维 |
| "想给下属提意见又怕打击他 / 想请教别人" | `hudong-xuexi-talks` 互动学习 TALKS |
| "最近学不下去，也说不清卡在哪" | `fansi-zhenduan` 反思与诊断 |

---

## 快速开始

安装后，直接对 Agent 说：

```
用四问学习法帮我分析我最近听的一本书，把它真正用起来
```

它会带你走一遍 **听 → 找 → 变 → 用**：你到底听到了什么、背后是什么模式、它让你哪个旧想法松动了、这周你会因此做一个什么具体的小改变。

已经知道要哪个工具时，也可以直接点名：

```
帮我发现这个问题背后的模式，再在模式指导下找原因
诊断一下我现在的学习在被动/主动/建构/互动/协作第几层
用互动学习 TALKS 帮我准备一次请教，把质疑变成请教
```

---

## 能力一览

一条主轴（四问学习法）贯穿始终，其余 7 个工具挂在它的某一步上，或作为排障/升级工具随手调用。

📌 **使用地图（一图看清 8 个 skill 的关系）**：[`skills/si-wen-xuexi-fa/assets/usage-map.svg`](skills/si-wen-xuexi-fa/assets/usage-map.svg)

| 工作目标 | 主要入口 | 角色 |
|---|---|---|
| 把听到/读到的知识用起来 | `si-wen-xuexi-fa` | ★ 主框架 / 枢纽 |
| 找问题背后的模式再找原因 | `faxian-moshi` | 第二步"找"的深化 |
| 决定学什么、学多少、聚焦哪 | `moshi-jujiao-xuexi` | 第一步"听"的取舍 |
| 换个想法、松动旧认知 | `cankao-daan-siwei` | 第三步"变"的思维底座 |
| 检验学习是否真发生 | `xuexi-tiwen` | 第四步"用"的试金石 |
| 诊断学习层级并升级 | `xuexi-fangshi-dengji` | 升级工具 |
| 讨论、请教、给/收反馈 | `hudong-xuexi-talks` | 互动工具 |
| 学不下去时排障 | `fansi-zhenduan` | 排障工具 |

完整关系图、推荐学习顺序见 [docs/INDEX.md](docs/INDEX.md)；不想读全书，看 [docs/DIGEST.md](docs/DIGEST.md)（精华长文，十几分钟串起 8 个工具）。

---

## 安装

### WorkBuddy / 豆包 / Codex 等支持 Skills 的 Agent

方式一（推荐，手动复制）：把 `skills/` 下的 8 个文件夹复制到你的用户级技能目录：

```bash
# WorkBuddy 示例（用户级，所有项目可用）
cp -r skills/* ~/.workbuddy/skills/
```

方式二（若你的 Agent 支持 skills CLI）：

```bash
npx -y skills add xiatian/xuehui-ruhe-xuexi-skills -g --all
```

### Claude Code 插件市场

```bash
claude plugin marketplace add xiatian/xuehui-ruhe-xuexi-skills
claude plugin install si-wen-xuexi-fa@xuehui-ruhe-xuexi-skills
```

> 安装命令中的默认用户名为 `xiatian`；若你的 GitHub 用户名不同，把它替换掉即可。

---

## 怎样工作

```
一段"听过却没用起来"的知识 / 一个反复出现的问题
        ↓
① 听 —— 如实接收，先说清你听到了什么
        ↓
② 找 —— 先发现模式，再在模式指导下找原因/答案（faxian-moshi）
        ↓
③ 变 —— 用参考答案思维松动旧想法（cankao-daan-siwei）
        ↓
④ 用 —— 落到本周一个具体的小改变（用不起来的学习是假学习）
        ↓
学不下去→ fansi-zhenduan ｜ 想升级→ xuexi-fangshi-dengji ｜ 要请教→ hudong-xuexi-talks
```

---

## 项目结构

```
xuehui-ruhe-xuexi-skills/
├── skills/                     # 8 个可直接调用的 Skills（每个 = 一个文件夹）
│   ├── si-wen-xuexi-fa/        # ★ 主框架，含 assets/usage-map.svg 使用地图
│   ├── faxian-moshi/
│   ├── moshi-jujiao-xuexi/
│   ├── xuexi-fangshi-dengji/
│   ├── xuexi-tiwen/
│   ├── cankao-daan-siwei/
│   ├── hudong-xuexi-talks/
│   └── fansi-zhenduan/         # 每个含 SKILL.md + test-prompts.json
├── docs/                       # DIGEST（精华长文）/ INDEX（索引与关系图）/ GLOSSARY（术语）/ test-results（盲测报告）
├── .claude-plugin/             # Claude Code 插件市场定义
├── LICENSE                     # CC BY-NC 4.0 + 来源声明
└── VERSION
```

每个 SKILL.md 采用 RIA++ 六段结构：R(原文≤150字) / I(方法论骨架) / A1(书中案例) / A2(触发场景) / E(可执行步骤) / B(边界)。

---

## 来源与许可

- **原书**：刘澜《学会如何学习：120堂认知升级课》，机械工业出版社，2025。
- 本仓库是**读者个人学习用途**的方法论蒸馏，非官方、不含原书完整内容，每处原文引用控制在 ≤150 字（合理使用）。
- 许可：[CC BY-NC 4.0](LICENSE) —— 个人学习/研究/非商业可自由使用，需署名；商业用途需另获原书权利方授权。
- 若你是权利方并认为某处引用不妥，请提 Issue，将立即处理。

## 致谢

感谢刘澜老师的《学会如何学习》。这套工具的全部方法论归功于原书，本仓库只做了"让它随手可调"的整理工作。
