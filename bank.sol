// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Bank {
    address public accHolder;
    uint256 public balance;  // Updated to public to track deposits publicly

    // Constructor accepts an initial deposit if provided
    constructor() payable {
        accHolder = msg.sender;
        balance = msg.value;  // Initialize balance with the deployment value
    }

    // Withdraw function to transfer the entire balance to the account holder
    function withdraw() public {
        require(msg.sender == accHolder, "You are not the account owner.");
        require(balance > 0, "You don't have enough balance.");

        uint256 amount = balance;
        balance = 0;  // Reset balance before transferring to avoid reentrancy issues
        payable(msg.sender).transfer(amount);  // Transfer the balance to accHolder
    }

    // Deposit function to increase the balance with the msg.value sent in the transaction
    function deposit() public payable {
        require(msg.sender == accHolder, "You are not the account owner.");
        require(msg.value > 0, "Deposit amount should be greater than 0.");

        balance += msg.value;  // Increase balance by msg.value
    }

    // View function to show the balance in the contract
    function showBalance() public view returns (uint256) {
        require(msg.sender == accHolder, "You are not the account owner.");
        return balance;
    }
}