import discord
from discord.ext import commands
from sys import argv

class Assistance:
    """
    Commands that will mostly be used in #help-and-questions.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True, name="sr", hidden=True)
    async def staffreq(self, ctx, *, msg_request=""):
        """Request staff, with optional additional text. Helpers, Staff, Verified only."""
        author = ctx.message.author
        if (self.bot.helpers_role not in author.roles) and (self.bot.staff_role not in author.roles) and (self.bot.verified_role not in author.roles) and (self.bot.trusted_role not in author.roles):
            msg = "{0} You cannot used this command at this time. Please ask individual staff members if you need help.".format(author.mention)
            await self.bot.say(msg)
            return
        await self.bot.delete_message(ctx.message)
        # await self.bot.say("Request sent.")
        msg = "❗️ **Assistance requested**: {0} by {1} | {2}#{3} @here".format(ctx.message.channel.mention, author.mention, author.name, ctx.message.author.discriminator)
        if msg_request != "":
            # msg += "\n✏️ __Additional text__: " + msg_request
            embed = discord.Embed(color=discord.Color.gold())
            embed.description = msg_request
        await self.bot.send_message(self.bot.mods_channel, msg, embed=(embed if msg_request != "" else None))
        await self.bot.send_message(author, "✅ Online staff has been notified of your request in {0}.".format(ctx.message.channel.mention), embed=(embed if msg_request != "" else None))

    @commands.command(pass_context=True)
    async def guide(self, ctx, *, console="auto"):
        """Links to Plailect's or FlimFlam69's guide."""
        console == console.lower()
        if console == "3ds" or (console == "auto" and "wiiu" not in ctx.message.channel.name):
            embed = discord.Embed(title="Guide", color=discord.Color(0xCE181E))
            embed.set_author(name="Plailect", url="https://3ds.guide/")
            embed.set_thumbnail(url="https://3ds.guide/images/bio-photo.png")
            embed.url = "https://3ds.guide/"
            embed.description = "A complete guide to 3DS custom firmware, from stock to arm9loaderhax."
            await self.bot.say("", embed=embed)
        if (console == "wiiu" or console == "wii u") or (console == "auto" and "3ds" not in ctx.message.channel.name):
            embed = discord.Embed(title="Guide", color=discord.Color(0x009AC7))
            embed.set_author(name="FlimFlam69", url="https://github.com/FlimFlam69/WiiUTutorial/wiki")
            embed.set_thumbnail(url="http://i.imgur.com/86Hm0kM.png")
            embed.url = "https://github.com/FlimFlam69/WiiUTutorial/wiki"
            embed.description = "FlimFlam69's 5.5.1 IOSU + Kernel Exploit Guide"
            await self.bot.say("", embed=embed)

    #Embed to Soundhax Download Website
    @commands.command()
    async def soundhax(self):
        """Links to Soundhax Website"""
        embed = discord.Embed(title="Soundhax", color=discord.Color.blue())
        embed.set_author(name="Ned Williamson", url="http://soundhax.com/")
        embed.set_thumbnail(url="http://i.imgur.com/lYf0jan.png")
        embed.url = "http://soundhax.com"
        embed.description = "Free 3DS Primary Entrypoint <= 11.2"
        await self.bot.say("", embed=embed)

    @commands.command()
    async def ez(self):
        """Links to ez3ds."""
        await self.simple_embed("Start here to discover how to hack your 3DS: https://ez3ds.xyz")

    # 9.6 xml command
    @commands.command()
    async def xmls(self):
        """Outputs XMLs for 3DS 9.6-crypto titles, for use with *hax 2.7+"""
        embed = discord.Embed(title="*hax 2.7 mmap XML repository for 9.6-crypto titles", color=discord.Color.green())
        embed.set_author(name="ihaveamac", url="https://github.com/ihaveamac", icon_url="https://avatars0.githubusercontent.com/u/590576?v=3&s=40")
        embed.description = "This is no longer necessary. Use *hax 2.8."
        embed.url = "https://github.com/ihaveamac/9.6-dbgen-xmls"
        await self.bot.say("", embed=embed)

    # dsp dumper command
    @commands.command()
    async def dsp(self):
        """Links to DspDump."""
        embed = discord.Embed(title="DspDump", color=discord.Color.green())
        embed.set_author(name="Cruel", url="https://github.com/Cruel", icon_url="https://avatars0.githubusercontent.com/u/383999?v=3&s=40")
        embed.description = "Dump 3DS's DSP component to SD for homebrew audio."
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Cruel/DspDump/master/icon.png")
        embed.url = "https://github.com/Cruel/DspDump/releases/latest"
        await self.bot.say("", embed=embed)


    @commands.command()
    async def update(self):
        """Explains how to safely prepare for an update if you have arm9loaderhax installed"""
        await self.simple_embed("If you have arm9loaderhax and Luma3DS installed after following Plailect's guide, run Luma Updater to make sure it is on the latest Luma3DS normal version and then you can proceed to update your 3DS through system settings. \nNTR CFW works on the latest version; use this version of BootNTR: \n<https://github.com/Nanquitas/BootNTR/releases>")

    # gateway h&s troubleshooting command
    @commands.command()
    async def gwhs(self):
        """Links to gateway health and safety inject troubleshooting"""
        await self.bot.say("https://3ds.guide/troubleshooting#gw_fbi")

    # hardmodder pastebin list
    @commands.command()
    async def hmodders(self):
        """Links to approved hardmodder list"""
        await self.simple_embed("Don't want to hardmod yourself? Ask one of the installers on the server! <https://pastebin.com/chh0hHPk>")

    @commands.command()
    async def builds(self):
        """Links to astronautlevel's luma commit site."""
        await self.simple_embed("Astronautlevel's Luma3DS commit builds can be found here: https://astronautlevel2.github.io/Luma3DS \n(Warning: most builds here are meant for developers and are untested, use at your own risk!)")

    # Links to 9.2 ctrtransfer guide
    @commands.command()
    async def ctr92(self):
        """Links to ctrtransfer guide"""
        #await self.simple_embed("https://3ds.guide/9.2.0-ctrtransfer")
        embed = discord.Embed(title="Guide - 9.2.0 ctrtransfer", color=discord.Color.orange())
        embed.set_author(name="Plailect", url="https://3ds.guide/")
        embed.set_thumbnail(url="https://3ds.guide/images/bio-photo.png")
        embed.url = "https://3ds.guide/9.2.0-ctrtransfer"
        embed.description = "How to do the 9.2.0-20 ctrtransfer"
        await self.bot.say("", embed=embed)

    @commands.command()
    async def s4guide(self):
        """Links to a guide for Sm4sh 3ds mods."""
        await self.simple_embed("A guide to setting up mods for smash on your 3ds can be found here: https://github.com/KotuMF/Smash-3DS-Modding-Guide/wiki")

    @commands.command(pass_context=True, name="ez2")
    async def ez2(self, ctx, model: str, major: int, minor: int, revision: int, nver: int, region: str, ):
        """Gives you the direct link to your version's page.\nExample: !ez2 Old 11 0 0 33 E"""
        await self.simple_embed("https://ez3ds.xyz/checkfw?model={0}&major={1}&minor={2}&revision={3}&nver={4}&region={5}".format(model, major, minor, revision, nver, region))

    @commands.command()
    async def brick(self):
        """Warns not to close the lid"""
        await self.simple_embed("**NEVER** shut the N3DS lid, **UPDATE** or **FORMAT** while on 2.1. The last two apply regardless of system model. Doing any of these things will cause serious system instability or outright brick your system.", color=discord.Color.red())

    @commands.command()
    async def downgrade(self):
        """Downgrade help"""
        await self.simple_embed("Follow Plailect's guide here: <https://3ds.guide/get-started>", title="Downgrade methods on 11.2 or below:")

    @commands.command()
    async def inoriquest(self):
        """Tells user to be descriptive"""
        await self.simple_embed("> Reminder: if you would like someone to help you, please be as descriptive as possible, of your situation, things you have done, as little as they may seem, aswell as assisting materials. Asking to ask wont expedite your process, and may delay assistance.")

    @commands.command()
    async def vguides(self):
        """Information about video guides relating to custom firmware"""
        embed = discord.Embed(title="Why you should not use video guides", color=discord.Color.dark_orange())
        embed.description = "\"Video guides\" for custom firmware and arm9loaderhax are not recommended for use. Their contents generally become outdated very quickly for them to be of any use, and they are harder to update unlike a written guide.\n\nWhen this happens, video guides become more complicated than current methods, having users do certain tasks which may not be required anymore.\n\nThere is also a risk of the uploader spreading misinformation or including potentially harmful files, sometimes unintentionally. Using other people's files to install arm9loaderhax can cause serious issues and even brick your system."
        embed.add_field(name="Recommended", value="The recommended thing to do is to use [Plailect's written complete guide for arm9loaderhax](https://3ds.guide). It is the most up to date one and is recommended for everyone.")
        await self.bot.say("", embed=embed)

    @commands.command()
    async def ip(self):
        """How to check your IP"""
        await self.simple_embed("1. FBI\n2. Remote Install\n3. Recieve URLs over the network", title="Check your 3DSs IP")

    @commands.command()
    async def ip2(self):
        """Homebrew way to know your IP"""
        await self.simple_embed("1. Open Homebrew Launcher\n2. Press Y", title="Check your 3DSs IP")

    @commands.command()
    async def nonandbackup(self):
        """Help when you missed the nand backup"""
        await self.simple_embed("1. When reached the section IV(4) from Installing arm9loaderahx replace the sections IV(4) & V(5) with https://3ds.guide/9.2.0-ctrtransfer.", title="If you missed the NAND Backup:")

    @commands.command()
    async def hbl113(self):
        """Get homebrew launcher working on 11.3"""
        await self.simple_embed("If you are on a CFW New 3DS you should disable the 'Clock + L2' on the Luma config(select on boot).")

    @commands.command()
    async def readguide(self):
        """Read the guide please"""
        await self.simple_embed("Asking something that is on the guide will make everyone lose time, so please read and re-read the guide steps 2 or 3 times before coming here.", title="Please read the guide")

    @commands.command()
    async def bigsd(self):
        """SD bigger than 32GB"""
        await self.simple_embed("If you want to change your SD card to one bigger than 32GB then you'll have to format it to FAT32.\nYou can do this with the tool of your preference.\nFormatter examples:\n- [guiformat](http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm)\n- gparted(for Linux users)", title="Big SD cards")
		##Kirito -Start-
    @commands.command()
    async def sderrors(self):
        """Sd Error Guide"""
        await self.simple_embed("Guide For Checking SDCard For Errors\n- [H2TestW Guide - Windows](https://3ds.guide/h2testw-(windows\))\n- [F3 Guide - Linux](https://3ds.guide/f3-(linux\))\n- [F3X Guide - Mac](https://3ds.guide/f3x-(mac\))", title="Sd Card Errors")		
	#old .ntrstream command had incorrect info
    @commands.command()
    async def ntrstream(self):
        """N3DS NTR Streaming Guide"""
        embed = discord.Embed(title="NTR CFW Streaming Guide", color=discord.Color.orange())
        embed.description = "(New Nintendo 3DS only) \n \n _1_ - Download the latest BootNTRSelector.cia from [BOOTNTRSelector](https://gbatemp.net/threads/release-bootntr-selector.432911/) (Use QR code if you wish)\n \n _2_ - download Kit-Kat From [Kit-Kat](https://gbatemp.net/threads/release-kit-kat-the-ultimate-3ds-toolkit-pc-client.453015/) (Put kit-kat.exe on desktop or wherever you choose) \n \n _3_ - Open BootNTR Selector And Follow On Screen Instructions (Use Default). Once It Has Asked You To Reboot Open BootNTR Selector and tap Use Default Then 3.4 Once That Has Happened Boot Out Of The App And Press X+Y If NTR CFW pops up on bottom screen your all set now to hop back onto the computer \n \n _4_ - Open Kit-Kat.exe And It Should automatically detect your Nintendo 3ds Local IP. goto settings and select Quality = 80. Priority Factor = 2. Quality Of Service Value = 101. Screen Priority = 1. (Other Options Are Your Personal Preference) Then Press Connect You Should See Your 3ds screen pop up or NTRviewer.exe needs admin permissions just click yes and you 3ds will pop up in a window \n \n _5_ - Record! or Stream! use whatever recording/streaming software you wish "	
        await self.bot.say("", embed=embed)
	    ##Kirito -End-
    @commands.command()
    async def notbricked(self):
        """Missing arm9loaderhax.bin"""
        await self.simple_embed("If your power LED turns on and off after you installed a9lh, you are not bricked and are just missing a file called arm9loaderhax.bin in the root of your SD card.\nTo fix this you should:\n1.Check you inserted the SD card in your console\n2.Place/replace the file, downloading it from https://github.com/AuroraWright/Luma3DS/releases\nChecking your SD for errors or corruption:\n\tWindows: https://3ds.guide/h2testw-(windows)\n\tLinux: https://3ds.guide/f3-(linux)\n\tMac: https://3ds.guide/f3x-(mac)", title="No. You are not bricked")

    @commands.command()
    async def emureco(self):
        """Recommendation about EmuNAND"""
        await self.simple_embed("If you want to set up an EmuNAND the first thing to know is that you probably don't need it; if you don't know what an EmuNAND is, you don't need one.", title="EmuNAND Recommendation")

    @commands.command()
    async def failedupdate(self):
        """Notice about failed update on Wii U"""
        await self.simple_embed("A failed update in Download Management does not mean there is an update and the system is trying to download it. This means your blocking method (DNS etc.) is working and the system can't check for an update.", color=discord.Color(0x009AC7))

    @commands.command()
    async def netinfo(self):
        """Network Maintenance Information / Operational Status"""
        await self.bot.say("https://www.nintendo.co.jp/netinfo/en_US/index.html")
        
    @commands.command()
    async def ctrmount(self):
        """Failed to mount CTRNAND error"""
        await self.simple_embed("While following the guide, after installing arm9loaderhax, if you get an error that says \"Failed to mount CTRNAND\", just continue on with the guide.")

def setup(bot):
    bot.add_cog(Assistance(bot))
