import read, copy
from util import *
from logical_classes import *

verbose =0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB

        Args:
            fact_rule (Fact|Rule) - the fact or rule to be added

        Returns:
            None
        """
        printv("Adding {!r}", 0, verbose, [fact_rule])
        #print "adding ", fact_rule
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                        #print "alert************\n", self.facts[ind]

        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)

    def kb_assert(self, statement):
        """Assert a fact or rule into the KB

        Args:
            statement (Statement): Statement we're asserting in the format produced by read.py
        """
        printv("Asserting {!r}", 1, verbose, [statement])
        self.kb_add(Fact(statement) if factq(statement) else Rule(statement))

    def kb_ask(self, statement):
        """Ask if a fact is in the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        printv("Asking {!r}", 0, verbose, [statement])
        if factq(statement):
            f = Fact(statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else False

        else:
            print "Invalid ask:", statement
            return False

    def kb_del(self, fact_rule):
        """delete a fact or rule to the KB

        Args:
            fact_rule (Fact|Rule) - the fact or rule to be deleted

        Returns:
            None
        """
        printv("deleting {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            ind = self.facts.index(fact_rule)
            if not self.facts[ind].supported_by:
                self.facts.pop(ind)

        elif isinstance(fact_rule, Rule):
            ind = self.rules.index(fact_rule)
            if not self.rules[ind].supported_by:
                self.rules.pop(ind)

    def kb_retract(self, statement):
        """Retract a fact from the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            None
        """
        printv("Retracting {!r}", 1, verbose, [statement])
        #print "retracting!!!!!!!!!"
        ####################################################
        # Student code goes here
        delStatement = Statement(statement)
        for fact in self.facts:
            if fact.statement == delStatement:
                # print "deleting" + delStatement.__str__()
                if fact.asserted == True:
                    fact.asserted = False
                    if fact.supported_by:
                        return
                for parFR in fact.supported_by:
                    parFR[0].supports_facts.remove(fact)
                    parFR[1].supports_facts.remove(fact)
                queue = [fact]
                while queue:
                    curFR = queue.pop(0)
                    queue += curFR.supports_facts + curFR.supports_rules
                    #print "deleting", curFR
                    for tempFR in queue:
                        for tempFRpair in tempFR.supported_by:
                            if tempFRpair[1] == curFR or tempFRpair[0] == curFR:
                                #print "remove supported by"
                                tempFR.supported_by.remove(tempFRpair)
                    
                    self.kb_del(curFR)
                        #print "deleting", curFR
                return
        

class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing            
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here
        bindings = match(fact.statement, rule.lhs[0])
        if bindings:
            # tempStatement = instantiate(fact.statement, bindings)
            # tempFact = Fact(tempStatement, [[rule, fact]])
            # fact.supports_facts.append(tempFact)
            # rule.supports_facts.append(tempFact)
            # print "*****************", kb

            if len(rule.lhs) > 1:
                templhs = [instantiate(sm, bindings) for sm in rule.lhs[1:]]
                temprhs = instantiate(rule.rhs, bindings)
                tempRule = Rule([templhs, temprhs], [[rule, fact]])

                rule.supports_rules.append(tempRule)
                fact.supports_rules.append(tempRule)

                kb.kb_add(tempRule)
            else:
                temprhs = instantiate(rule.rhs, bindings)
                tempFact = Fact(temprhs, [[rule, fact]])

                rule.supports_facts.append(tempFact)
                fact.supports_facts.append(tempFact)
                kb.kb_add(tempFact)



