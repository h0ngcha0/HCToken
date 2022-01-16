from brownie import HCToken, config, network
from scripts.helper_script import get_account

def deploy_lottery():
    account = get_account()
    ourToken = HCToken.deploy(
        100000000000000000000,
        {"from": account},
        publish_source = config["networks"][network.show_active()].get("verify", False),
    )

    print("Deployed ERC20")
    return ourToken

def main():
    deploy_lottery()