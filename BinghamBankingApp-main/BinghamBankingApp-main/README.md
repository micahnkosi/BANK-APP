1. *BankAccount Class*: This is the base class with basic functionalities like deposit, withdraw, and checking balance.
2. *SavingsAccount Class*: Inherits from BankAccount, adds interest on deposits, and has a withdrawal limit.
3. *CurrentAccount Class*: Inherits from BankAccount, with no restrictions.
4. *ChildrensAccount Class*: Inherits from BankAccount, adds a higher interest rate on deposits, and restricts withdrawals.
5. *StudentAccount Class*: Inherits from BankAccount, imposes limits on both deposits and withdrawals.

### Key OOP Concepts:
- *Inheritance*: The specific account types inherit from the general BankAccount class.
- *Polymorphism*: Each account type can redefine the deposit and withdraw methods.
- *Encapsulation*: The _balance attribute is protected to prevent direct modification from outside the class, ensuring controlled access through methods.
