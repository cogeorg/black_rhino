#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from src.helper import Helper

# -------------------------------------------------------------------------
#  class Tests
# -------------------------------------------------------------------------


class TestsUpdater(object):
    #
    # VARIABLES
    #

    #
    # METHODS
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_info(text)
    # -------------------------------------------------------------------------
    def print_info(self, text):
        print('##############################################################################\n')
        print(text)
        print('##############################################################################\n')
    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR UPDATER.PY >> PAWEL TO DO <<
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_identifier
    # -------------------------------------------------------------------------

    def updater__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.identifier = "test_model_id"
        print("Model's ID:")
        print(model.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_identifier
    # -------------------------------------------------------------------------

    def updater__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.identifier = "test_model_id"
        print("Model's ID:")
        print(model.get_identifier())
        print("Changing model ID...")
        model.set_identifier("new_model_id")
        print("Model's ID:")
        print(model.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_model_parameters
    # -------------------------------------------------------------------------

    def updater__get_model_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_model_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_model_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.model_parameters = {"test": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_model_parameters
    # -------------------------------------------------------------------------

    def updater__set_model_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_model_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_model_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.model_parameters = {"test": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())
        print("Changing model's parameters:...")
        model.model_parameters = {"new": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_interactions
    # -------------------------------------------------------------------------

    def updater__get_interactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_interactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_interactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        print("Model's interactions:")
        print(model.get_interactions())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_interactions
    # -------------------------------------------------------------------------

    def updater__set_interactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_interactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_interactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        print("Model's interactions:")
        print(model.get_interactions())
        print("Changing model's agents:...")
        model.set_interactions(["new", "interactions"])
        print("Model's interactions:")
        print(model.get_interactions())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__str
    # -------------------------------------------------------------------------

    def updater__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.str \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.identifier = "testing str"
        print(model.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__init
    # -------------------------------------------------------------------------

    def updater__init(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.init \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__init in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.__init__(environment)
        print(model.environment)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__accrue_interests
    # -------------------------------------------------------------------------

    def updater__accrue_interests(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.accrue_interests \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__accrue_interests in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        bank.interest_rate_deposits = 0.05
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.__init__(environment)
        environment.new_transaction("deposits", "",  environment.get_agent_by_id("test_household").identifier, environment.get_agent_by_id("test_bank"),
                                    10.0, environment.get_agent_by_id("test_bank").interest_rate_deposits,  0, -1)
        print(environment.get_agent_by_id("test_household"))
        print("Accruing interests\n")
        model.accrue_interests(environment, 0)
        print(environment.get_agent_by_id("test_household"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__maturities
    # -------------------------------------------------------------------------

    def updater__maturities(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.maturities \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__maturities in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        bank.interest_rate_deposits = 0.05
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.__init__(environment)
        environment.new_transaction("deposits", "",  environment.get_agent_by_id("test_household").identifier, environment.get_agent_by_id("test_bank"),
                                    10.0, environment.get_agent_by_id("test_bank").interest_rate_deposits,  0, -1)
        print(environment.get_agent_by_id("test_household"))
        model.maturities(environment, 1)
        print(environment.get_agent_by_id("test_household"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__amortisation
    # -------------------------------------------------------------------------

    def updater__amortisation(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.amortisation \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__amortisation in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        bank.interest_rate_deposits = 0.05
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.__init__(environment)
        environment.get_agent_by_id("test_firm").state_variables["capital"] = 20.0
        environment.get_agent_by_id("test_firm").parameters["amortisation"] = 0.1
        print(environment.get_agent_by_id("test_firm"))
        model.amortisation(environment, 1)
        print(environment.get_agent_by_id("test_firm"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_funding
    # -------------------------------------------------------------------------

    def updater__get_funding(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_funding \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_funding in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        bank.interest_rate_deposits = 0.05
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        model = Updater(environment)
        model.__init__(environment)
        environment.get_agent_by_id("test_firm").state_variables["funding"] = 20.0
        environment.get_agent_by_id("test_firm").state_variables["capital"] = 0.1
        environment.get_agent_by_id("test_firm").parameters["capital_elasticity"] = 0.4
        print(environment.get_agent_by_id("test_firm"))
        model.get_funding(environment, 1)
        print(environment.get_agent_by_id("test_firm"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__sell_labour
    # -------------------------------------------------------------------------

    def updater__sell_labour(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.sell_labour \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__sell_labour in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        print(environment.households[0])
        print("Selling labour")
        model.sell_labour(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__consume_rationed
    # -------------------------------------------------------------------------

    def updater__consume_rationed(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.consume_rationed \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__consume_rationed in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        model.sell_labour(environment, 0)
        print(environment.households[0])
        print("Consuming the production")
        model.consume_rationed(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__remove_perishable
    # -------------------------------------------------------------------------

    def updater__remove_perishable(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.remove_perishable \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__remove_perishable in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        print(environment.households[0])
        print("Removing perishable")
        model.remove_perishable(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__check_liquidity
    # -------------------------------------------------------------------------

    def updater__check_liquidity(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.check_liquidity \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__check_liquidity in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        model.remove_perishable(environment, 0)
        print(environment.households[0])
        print("Checking liquidity")
        model.check_liquidity(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__capitalise_new
    # -------------------------------------------------------------------------

    def updater__capitalise_new(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.capitalise_new \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__capitalise_new in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        print(environment.households[0])
        model.remove_perishable(environment, 0)
        print("Capitalising")
        model.capitalise_new(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__check_consistency
    # -------------------------------------------------------------------------

    def updater__check_consistency(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.check_consistency \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__check_consistency in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.get_funding(environment, 0)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        print(environment.households[0])
        model.remove_perishable(environment, 0)
        model.capitalise_new(environment, 0)
        print("Checking consistency")
        model.check_consistency(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__do_update
    # -------------------------------------------------------------------------

    def updater__do_update(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.do_update \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__do_update in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        print(environment.households[0])
        print("Doing update")
        model.do_update(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------
