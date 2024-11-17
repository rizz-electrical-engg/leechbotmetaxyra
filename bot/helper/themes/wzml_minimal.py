#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Owner'
    ST_BN1_URL = 'https://t.me/Noctophile'
    ST_BN2_NAME = 'Cloud🌩️Store'
    ST_BN2_URL = 'https://t.me/CloudStoreRizz'
    ST_MSG = '''<blockquote><b>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.Type {help_command} to get a list of available commands</b></blockquote>'''
    ST_BOTPM = '''<blockquote><i>Now, This bot will send all your files and links here. Start Using ...</blockquote></i>'''
    ST_UNAUTH = '''<blockquote><i>You Are not authorized user!</i></blockquote>'''
    OWN_TOKEN_GENERATE = '''<blockquote><b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i></blockquote>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<blockquote><b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i></blockquote>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''

    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = 'Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "🚨 <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<blockquote>⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</blockquote>
    
    '''
    SYS_STATS = '''<blockquote>⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}</blockquote>
    '''
    REPO_STATS = '''<blockquote>⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code></blockquote>
    '''
    BOT_LIMITS = '''<blockquote>⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}</blockquote>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<blockquote>🌋 <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}</blockquote>'''
    RESTARTED = '''<blockquote>🍁 <b><i>Bot Restarted!</i></b></blockquote>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Tunik🐾</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n</blockquote>"""
    LINKS_SOURCE = """<blockquote>➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n</blockquote>"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<blockquote><b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '┠ <b>Size: </b>{Size}\n'
    ELAPSE =                '┠ <b>Elapsed: </b>{Time}\n'
    MODE =                  '┠ <b>Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┖ <b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>Files: </b>{Files}\n'
    RCPATH =                '┠ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b></blockquote>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>Pʀᴏᴄᴇssᴇᴅ:</b> {Processed}'
    STATUS =            '\n┠ <b>Sᴛᴀᴛᴜs:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>Eᴛᴀ:</b> {Eta}'
    SPEED =             '\n┠ <b>Sᴘᴇᴇᴅ:</b> {Speed}'
    ELAPSED =                                     ' | <b>Eʟᴀᴘsᴇᴅ:</b> {Elapsed}'
    ENGINE =            '\n┠ <b>Eɴɢɪɴᴇ:</b> {Engine}'
    STA_MODE =          '\n┠ <b>Mᴏᴅᴇ:</b> {Mode}'
    SEEDERS =           '\n┠ <b>Sᴇᴇᴅᴇʀs:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>Sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>Sᴘᴇᴇᴅ: </b> {Speed} | '
    UPLOADED =                                     '<b>Uᴘʟᴏᴀᴅᴇᴅ: </b> {Upload}'
    RATIO =          '\n┠ <b>Rᴀᴛɪᴏ: </b> {Ratio} | '
    TIME =                                         '<b>Tɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>Sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>Usᴇʀ:</b> <code>{User}</code> | '
    ID =                                                        '<b>Iᴅ:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>Sᴇʟᴇᴄᴛ:</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>\n'
    TASKS =  '┠ <b>Tᴀsᴋs:</b> {Tasks}\n'
    BOT_TASKS = '┠ <b>Tᴀsᴋs:</b> {Tasks}/{Ttask} | <b>Aᴠʟ:</b> {Free}\n'
    Cpu = '┠ <b>Cᴘᴜ:</b> {cpu}% | '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>Rᴀᴍ:</b> {ram}% | '
    uptime =                     '<b>UᴘTɪᴍᴇ:</b> {uptime}'
    DL = '\n┖ <b>Dʟ:</b> {DL}/s | '
    UL =                        '<b>Uʟ:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '◀️'
    REFRESH = 'Pᴀɢᴇs\n{Page}'
    NEXT = '▶️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'Fɪʟᴇ/Fᴏʟᴅᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ Dʀɪᴠᴇ.\nHᴇʀᴇ ᴀʀᴇ {content} ʟɪsᴛ ʀᴇsᴜʟᴛs:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Cᴏᴜɴᴛɪɴɢ:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Sɪᴢᴇ: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Tʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SᴜʙFᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>Fɪʟᴇs: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>Bʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Sᴇᴀʀᴄʜɪɴɢ ғᴏʀ <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Fᴏᴜɴᴅ {NO} ʀᴇsᴜʟᴛ ғᴏʀ <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>Nᴏ Aᴄᴛɪᴠᴇ Dᴏᴡɴʟᴏᴀᴅs!\n Hᴀᴠᴇ A Nɪᴄᴇ Dᴀʏ😊</i>
    
⌬ <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>
┠ <b>Cᴘᴜ:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>Rᴀᴍ:</b> {ram} | <b>UᴘTɪᴍᴇ:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>Usᴇʀ Sᴇᴛᴛɪɴɢs :</u></b>
        
┎<b> Nᴀᴍᴇ : </b>{NAME} ( <code>{ID}</code> )
┠<b> Usᴇʀɴᴀᴍᴇ :</b> {USERNAME}
┖<b> Tᴇʟᴇɢʀᴀᴍ DC :</b> {DC}'''

    UNIVERSAL = '''㊂ <b><u>Uɴɪᴠᴇʀsᴀʟ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

┎<b> YT-DLP Oᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
┠<b> Dᴀɪʟʏ Tᴀsᴋs :</b> <code>{DT}</code> ᴘᴇʀ ᴅᴀʏ
┠<b> Lᴀsᴛ Bᴏᴛ Usᴇᴅ :</b> <code>{LAST_USED}</code>
┠<b> Usᴇʀ Sᴇssɪᴏɴ :</b> <code>{USESS}</code>
┠<b> MᴇᴅɪᴀIɴғᴏ Mᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
┠<b> Sᴀᴠᴇ Mᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
┖<b> Usᴇʀ Bᴏᴛ PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mɪʀʀᴏʀ/Cʟᴏɴᴇ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

┎<b> RCʟᴏɴᴇ Cᴏɴғɪɢ :</b> <i>{RCLONE}</i>
┠<b> Mɪʀʀᴏʀ Pʀᴇғɪx :</b> <code>{MPREFIX}</code>
┠<b> Mɪʀʀᴏʀ Sᴜғғɪx :</b> <code>{MSUFFIX}</code>
┠<b> Mɪʀʀᴏʀ Rᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
┠<b> DDL Sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
┠<b> Usᴇʀ TD Mᴏᴅᴇ :</b> <i>{TMODE}</i>
┠<b> Tᴏᴛᴀʟ Usᴇʀ TD(s) :</b> <i>{USERTD}</i>
┖<b> Dᴀɪʟʏ Mɪʀʀᴏʀ :</b> <code>{DM}</code> ᴘᴇʀ ᴅᴀʏ'''

    LEECH = '''㊂ <b><u>Lᴇᴇᴄʜ Sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

┎<b> Dᴀɪʟʏ Lᴇᴇᴄʜ :</b> <code>{DL}</code ᴘᴇʀ ᴅᴀʏ
┠<b> Lᴇᴇᴄʜ Tʏᴘᴇ :</b> <i>{LTYPE}</i>
┠<b> Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
┠<b> Lᴇᴇᴄʜ Sᴘʟɪᴛ Sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
┠<b> Eǫᴜᴀʟ Sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Mᴇᴅɪᴀ Gʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
┠<b> Lᴇᴇᴄʜ Cᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
┠<b> Lᴇᴇᴄʜ Pʀᴇғɪx :</b> <code>{LPREFIX}</code>
┠<b> Lᴇᴇᴄʜ Sᴜғғɪx :</b> <code>{LSUFFIX}</code>
┠<b> Lᴇᴇᴄʜ Dᴜᴍᴘs :</b> <code>{LDUMP}</code>
┠<b> Lᴇᴇᴄʜ Rᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>
┖<b> Mᴇᴛᴀᴅᴀᴛᴀ :</b> <code>{LMETA}</code>'''
