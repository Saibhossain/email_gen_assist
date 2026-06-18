DATASET = [
    {
        "id": 1,
        "intent": "Follow up after a discovery call",
        "key_facts": "- Enjoyed learning about their expansion into APAC\n- Attached our enterprise pricing sheet\n- Proposed a follow-up demo next Tuesday at 2 PM EST",
        "tone": "Formal",
        "human_reference": "Subject: Follow-Up: Enterprise Solutions for APAC Expansion\n\nDear Team,\n\nThank you for taking the time to speak with us during our discovery call. It was fascinating to learn more about your strategic expansion into the APAC region.\n\nAs requested, I have attached our enterprise pricing sheet to this email for your review. To help visualize how our platform can support your regional goals, I propose scheduling a comprehensive demo next Tuesday at 2 PM EST.\n\nPlease let me know if this time aligns with your schedule.\n\nBest regards,\nAccount Management Team"
    },
    {
        "id": 2,
        "intent": "Urgent bug fix deploy alert",
        "key_facts": "- Production hotfix deployed to patch memory leak\n- System downtime lasted 4 minutes\n- Post-mortem report will be shared tomorrow morning",
        "tone": "Urgent",
        "human_reference": "Subject: URGENT: Production Hotfix Deployed & Memory Leak Patched\n\nTeam,\n\nPlease be advised that an emergency production hotfix was just deployed successfully to remediate a critical memory leak.\n\nThis deployment required a brief system downtime lasting exactly 4 minutes. Operations are now fully restored, and performance metrics are stable.\n\nA complete post-mortem report will be shared tomorrow morning. Thank you for your swift coordination.\n\nRegards,\nEngineering Ops"
    },
    {
        "id": 3,
        "intent": "Reject a vendor proposal",
        "key_facts": "- Budget constraints for Q3\n- Decided to stay with current provider\n- Keep door open for next fiscal year evaluation",
        "tone": "Empathetic",
        "human_reference": "Subject: Update regarding your business proposal\n\nDear Partners,\n\nThank you so much for the time and effort invested in compiling your comprehensive vendor proposal. We were incredibly impressed by your team's capabilities.\n\nUnfortunately, due to unexpected budget constraints for Q3, we are unable to onboard new platforms at this time and have decided to renew with our current provider. We understand this news is disappointing, given the alignment we discovered.\n\nWe genuinely hope to keep the door open for future collaboration and re-evaluate your solutions during the next fiscal year.\n\nWarmly,\nProcurement Director"
    },
    {
        "id": 4,
        "intent": "Internal team sync invite",
        "key_facts": "- Review mid-year OKR progress\n- Bring coffee, informal setting\n- Meet in the main breakout lounge at 11 AM",
        "tone": "Casual",
        "human_reference": "Subject: OKR check-in & coffee this morning! \n\nHey everyone,\n\nLet's get together at 11 AM in the main breakout lounge to chat through our mid-year OKR progress and see where things stand.\n\nGrab a coffee on your way in—this is going to be super informal and low-key. See you all there!\n\nCheers,\nTeam Lead"
    },
    {
        "id": 5,
        "intent": "Request project extension approval",
        "key_facts": "- Client expanded scope to include mobile UI redesign\n- Need 10 additional engineering days\n- Revised delivery date target: Nov 20th",
        "tone": "Formal",
        "human_reference": "Subject: Formal Request for Project Extension: Mobile UI Scope Expansion\n\nDear Steering Committee,\n\nI am writing to formally request an adjustment to the timeline of our ongoing project. The client has recently expanded the scope of work to encompass a comprehensive mobile UI redesign.\n\nTo absorb this additional workload without sacrificing architectural quality, we require 10 additional engineering days. Consequently, we propose a revised delivery date target of November 20th.\n\nThank you for considering this request. I am available to discuss any resource reallocations.\n\nSincerely,\nDelivery Lead"
    },
    {
        "id": 6,
        "intent": "Congratulate employee on promotion",
        "key_facts": "- Promoted to Senior AI Architect\n- Exceptional execution on the multi-agent orchestration deployment\n- Effective starting first of next month",
        "tone": "Empathetic",
        "human_reference": "Subject: Congratulations on your promotion to Senior AI Architect!\n\nDear Sarah,\n\nI am absolutely thrilled to celebrate your promotion to Senior AI Architect, effective the first of next month.\n\nYour exceptional execution on the multi-agent orchestration deployment was masterclass-level work, and it set a new benchmark for technical excellence across our engineering org. Thank you for your leadership and dedication.\n\nWe are incredibly lucky to have you on this journey.\n\nWith deep appreciation,\nVP of Engineering"
    },
    {
        "id": 7,
        "intent": "Inquire about missing invoice payment",
        "key_facts": "- Invoice #2024-89B is 14 days overdue\n- Total outstanding balance is $14,500\n- Need processing confirmation within 48 hours",
        "tone": "Urgent",
        "human_reference": "Subject: OVERDUE NOTICE: Invoice #2024-89B ($14,500)\n\nDear Accounts Payable Team,\n\nThis notification concerns invoice #2024-89B, which is now 14 days overdue. The total outstanding balance of $14,500 remains unpaid on our records.\n\nPlease provide a payment processing confirmation within the next 48 hours to ensure no interruption to active contract services.\n\nThank you for your immediate attention to this matter.\n\nFinance Operations"
    },
    {
        "id": 8,
        "intent": "Announce annual company retreat",
        "key_facts": "- Location: Lisbon, Portugal\n- Dates: September 12-16\n- Flights must be booked through corporate portal by end of week",
        "tone": "Casual",
        "human_reference": "Subject: We're heading to Lisbon! ✈️ Retreat updates inside\n\nHey team!\n\nThe secret is out—our annual company retreat is happening in Lisbon, Portugal from September 12-16!\n\nWe need everyone to log into the corporate portal and book your flights by the end of this week so logic-ops can finalize hotels. Get ready for an amazing trip!\n\nBest,\nPeople Ops"
    },
    {
        "id": 9,
        "intent": "Request for Proposal (RFP) detailing cybersecurity services",
        "key_facts": "- Seeking SOC 2 compliance monitoring tools\n- Submission deadline is August 1st\n- Require vendor to present case studies of similar scale deployments",
        "tone": "Formal",
        "human_reference": "Subject: Request for Proposal (RFP): SOC 2 Cybersecurity Services\n\nTo Whom It May Concern,\n\nOur organization is formally issuing this Request for Proposal (RFP) for comprehensive cybersecurity services, specifically targeting automated SOC 2 compliance monitoring tools.\n\nAll formal proposals must be submitted through our portal no later than August 1st. Additionally, we require all responding vendors to present matching case studies of deployments at an equivalent enterprise scale.\n\nWe look forward to reviewing your submissions.\n\nSincerely,\nChief Information Security Officer"
    },
    {
        "id": 10,
        "intent": "Resignation notification to manager",
        "key_facts": "- Final working day will be July 31st\n- Transition plan will be fully documented this week\n- Grateful for mentorship during tenure",
        "tone": "Formal",
        "human_reference": "Subject: Formal Resignation - Final Day July 31st\n\nDear David,\n\nPlease accept this email as formal notification that I am resigning from my position. My final working day with the company will be July 31st.\n\nI am deeply grateful for your invaluable mentorship and support during my tenure here. To ensure a seamless handover, I will completely document my current transition plan by the end of this week.\n\nThank you again for everything.\n\nSincerely,\nMichael"
    }
]