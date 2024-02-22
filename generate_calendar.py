from ics import Calendar, Event
from datetime import datetime, timedelta

# you can add events as you need 
airdrop_events = [
    ("Namada", "2024-03-15", "TGE"),
    ("AltLayer", "2024-01-20", "TGE"),
    ("Dymension", "2024-02-10", "Airdrop"),
    ("Saga", "2024-04-01", "Airdrop"), 
    ("Frame", "2024-04-01","Airdrop"), 
    ("Aevo", "2024-01-15","TGE"),
    ("Thetanuts Finance", "2024-03-01","Airdrop"),
    ("zkLink", "2024-03-01","TGE"),
    ("ZetaChain", "2024-03-01","TGE"),
    ("Marginfi Airdrop", "2024-04-01","Speculated early airdrop among projects."),
    ("Kamino Genesis Airdrop","2024-04-01", "Kamino's first season points activity and genesis airdrop planned for April."),
    ("Drift Airdrop","2024-04-01","Drift's first season points ended on Feb 2; airdrop likely in April."),
    ("Parcl Airdrop","2024-06-01", "Parcl's second season points ongoing; airdrop hinted after season end."),
    ("Zeta Markets Airdrop","2024-03-01","Zeta Markets' second season points activity started on Jan 10."),
    ("Magic Eden Airdrop","2024-02-28","Magic Eden multi-chain wallet users can mint certain NFTs for free in February."),
    # Sui Ecosystem
    ("Scallop Airdrop", "2024-04-01", "Ongoing points system in Scallop, Sui ecosystem."),
    ("Bluefin Airdrop", "2024-04-01", "Bluefin, a derivatives protocol in Sui ecosystem."),
    ("Bucket Protocol Airdrop", "2024-04-01", "Bucket Protocol, a stablecoin protocol in Sui."),
    ("Suilend Airdrop", "2024-02-14", "Suilend lending platform launch on Sui."),
    ("Volo Airdrop", "2024-04-01", "Volo liquidity staking in Sui ecosystem."),
    ("Haedal Airdrop", "2024-04-01", "Haedal liquidity staking in Sui ecosystem."),
    # Ethereum L2 and Other Public Blockchains
    ("Berachain Airdrop", "2024-04-01", "Berachain's unique design and ecosystem focus."),
    ("Orderly Network Airdrop", "2024-04-01", "Settlement layer protocol in modular blockchain."),
    ("Aleo Airdrop", "2024-03-31", "A privacy-focused L1 blockchain."),
    ("Fuel Airdrop", "2024-04-01", "UTXO-based modular execution layer."),
    ("Avail Airdrop", "2024-03-31", "Polygon's data availability-focused blockchain."),
    ("Quai Network Airdrop", "2024-06-01", "EVM-compatible L1 blockchain."),
    ("zkSync Airdrop", "2024-04-01", "One of the Ethereum L2 'big four'."),
    ("Blast Airdrop", "2024-04-01", "Popular deposit-for-points project."),
    ("Linea Airdrop", "2024-04-01", "Ethereum L2 developed by ConsenSys."),
    ("Taiko Airdrop", "2024-03-31", "EVM-equivalent ZK Rollup."),
     # Re-Staking Sector
    ("EigenLayer Staking Window", "2024-02-06", "Reopening of staking with new LSTs."),
    ("Kelp DAO and Swell Points Acceleration", "2024-02-10", "Points acceleration event."),
    ("Puffer Finance Staking", "2024-01-30", "Staking opened with significant TVL."),
    ("Eigenpie Staking Benefits", "2024-02-15", "Staking swETH yields multiple rewards."),
    # DeFi Sector
    ("Curvance Testnet Participation", "2024-03-01", "Participation in Curvance's testnet."),
    ("Kinza Points System and Airdrop", "2024-03-31", "Points system launch and planned airdrop."),
    ("KiloEx Points System and TGE", "2024-06-01", "Introduction of points system and TGE planning."),
    ("Doubler Testnet Activity", "2024-02-01", "Doubler's activity on the Blast testnet."),
    # Other Projects
    ("LayerZero V2 Launch", "2024-04-01", "Launch of LayerZero's V2 version."),
    ("Wormhole Integration and Funding", "2024-04-15", "Integration with Dymension and funding."),
    ("DappOS Development Stage", "2024-05-01", "Development stage and expected token launch."),
    ("Pyth Network Airdrop Opportunities", "2024-05-15", "Potential airdrops for $PYTH stakers."),
    ("Farcaster Development and Funding", "2024-06-01", "Development progress and seed funding."),
]

# create a calendar
cal = Calendar()

# add calendars for events
for event in airdrop_events:
    name, date, details = event  # Adjusted to match the (name, date, details) format
    event = Event()
    event.name = name
    event.begin = datetime.strptime(date, "%Y-%m-%d")
    event.duration = timedelta(days=1)  # Assuming the event lasts for 1 day
    event.description = details
    cal.events.add(event)

# save as ICS file
with open("Airdrop_Calendar.ics", "w") as f:
    f.writelines(cal.serialize())
