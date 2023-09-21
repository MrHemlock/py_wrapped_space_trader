
from __future__ import annotations

from enum import auto, StrEnum
from datetime import datetime
from typing import Annotated, Any, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
)
from pydantic.alias_generators import to_camel


class SymbolEnums(StrEnum):
    @staticmethod
    def _generate_next_value_(
        name: str,
        start: int,
        count: int,
        last_values: list[Any],
    ) -> Any:
        return name.upper()


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)


class ContractType(SymbolEnums):
    PROCURMENT = auto()
    TRANSPORT = auto()
    SHUTTLE = auto()


class DepositType(SymbolEnums):
    QUARTZ_SAND = auto()
    SILICON_CRYSTALS = auto()
    PRECIOUS_STONES = auto()
    ICE_WATER = auto()
    AMMONIA_ICE = auto()
    IRON_ORE = auto()
    COPPER_ORE = auto()
    SILVER_ORE = auto()
    ALUMINUM_ORE = auto()
    GOLD_ORE = auto()
    PLATINUM_ORE = auto()
    DIAMONDS = auto()
    URANITE_ORE = auto()
    MERITIUM_ORE = auto()


class FactionSymbols(SymbolEnums):
    COSMIC = auto()
    VOID = auto()
    GALACTIC = auto()
    QUANTUM = auto()
    DOMINION = auto()
    ASTRO = auto()
    CORSAIRS = auto()
    OBSIDIAN = auto()
    AEGIS = auto()
    UNITED = auto()
    SOLITARY = auto()
    OMEGA = auto()
    ECHO = auto()
    LORDS = auto()
    CULT = auto()
    ANCIENTS = auto()
    SHADOW = auto()
    ETHERAL = auto()


class FactionTraitSymbols(SymbolEnums):
    BUREAUCRATIC = auto()
    SECRETIVE = auto()
    CAPITALISTIC = auto()
    INDUSTRIOUS = auto()
    PEACEFUL = auto()
    DISTRUSTFUL = auto()
    WELCOMING = auto()
    SMUGGLERS = auto()
    SCAVENGERS = auto()
    REBELLIOUS = auto()
    EXILES = auto()
    PIRATES = auto()
    RAIDERS = auto()
    CLAN = auto()
    GUILD = auto()
    DOMINION = auto()
    FRINGE = auto()
    FORSAKEN = auto()
    ISOLATED = auto()
    LOCALIZED = auto()
    ESTABLISHED = auto()
    NOTABLE = auto()
    DOMINANT = auto()
    INESCAPABLE = auto()
    INNOVATIVE = auto()
    BOLD = auto()
    VISIONARY = auto()
    CURIOUS = auto()
    DARING = auto()
    EXPLORATORY = auto()
    RESOURCEFUL = auto()
    FLEXIBLE = auto()
    COOPERATIVE = auto()
    UNITED = auto()
    STRATEGIC = auto()
    INTELLIGENT = auto()
    RESEARCH_FOCUSED = auto()
    COLLABORATIVE = auto()
    PROGRESSIVE = auto()
    MILITARISTIC = auto()
    TECHNOLOGICALLY_ADVANCED = auto()
    AGGRESSIVE = auto()
    IMPERIALISTIC = auto()
    TREASURE_HUNTERS = auto()
    DEXTEROUS = auto()
    UNPREDICTABLE = auto()
    BRUTAL = auto()
    FLEETING = auto()
    ADAPTABLE = auto()
    SELF_SUFFICIENT = auto()
    DEFENSIVE = auto()
    PROUD = auto()
    DIVERSE = auto()
    INDEPENDENT = auto()
    SELF_INTERESTED = auto()
    FRAGMENTED = auto()
    COMMERCIAL = auto()
    FREE_MARKETS = auto()
    ENTREPRENEURIAL = auto()


class MarketSupply(SymbolEnums):
    SCARCE = auto()
    LIMITED = auto()
    MODERATE = auto()
    ABUNDANT = auto()


class ShipType(SymbolEnums):
    SHIP_PROBE = auto()
    SHIP_MINING_DRONE = auto()
    SHIP_INTERCEPTOR = auto()
    SHIP_LIGHT_HAULER = auto()
    SHIP_COMMAND_FRIGATE = auto()
    SHIP_EXPLORER = auto()
    SHIP_HEAVY_FREIGHTER = auto()
    SHIP_LIGHT_SHUTTLE = auto()
    SHIP_ORE_HOUND = auto()
    SHIP_REFINING_FREIGHTER = auto()


class ShipEngineType(SymbolEnums):
    ENGINE_IMPULSE_DRIVE_I = auto()
    ENGINE_ION_DRIVE_I = auto()
    ENGINE_ION_DRIVE_II = auto()
    ENGINE_HYPER_DRIVE_I = auto()


class ShipFrameType(SymbolEnums):
    FRAME_PROBE = auto()
    FRAME_DRONE = auto()
    FRAME_INTERCEPTOR = auto()
    FRAME_RACER = auto()
    FRAME_FIGHTER = auto()
    FRAME_FRIGATE = auto()
    FRAME_SHUTTLE = auto()
    FRAME_EXPLORER = auto()
    FRAME_MINER = auto()
    FRAME_LIGHT_FREIGHTER = auto()
    FRAME_HEAVY_FREIGHTER = auto()
    FRAME_TRANSPORT = auto()
    FRAME_DESTROYER = auto()
    FRAME_CRUISER = auto()
    FRAME_CARRIER = auto()


class ShipModuleType(SymbolEnums):
    MODULE_MINERAL_PROCESSOR_I = auto()
    MODULE_CARGO_HOLD_I = auto()
    MODULE_CREW_QUARTERS_I = auto()
    MODULE_ENVOY_QUARTERS_I = auto()
    MODULE_PASSENGER_CABIN_I = auto()
    MODULE_MICRO_REFINERY_I = auto()
    MODULE_ORE_REFINERY_I = auto()
    MODULE_FUEL_REFINERY_I = auto()
    MODULE_SCIENCE_LAB_I = auto()
    MODULE_JUMP_DRIVE_I = auto()
    MODULE_JUMP_DRIVE_II = auto()
    MODULE_JUMP_DRIVE_III = auto()
    MODULE_WARP_DRIVE_I = auto()
    MODULE_WARP_DRIVE_II = auto()
    MODULE_WARP_DRIVE_III = auto()
    MODULE_SHIELD_GENERATOR_I = auto()
    MODULE_SHIELD_GENERATOR_II = auto()


class ShipMountType(SymbolEnums):
    MOUNT_GAS_SIPHON_I = auto()
    MOUNT_GAS_SIPHON_II = auto()
    MOUNT_GAS_SIPHON_III = auto()
    MOUNT_SURVEYOR_I = auto()
    MOUNT_SURVEYOR_II = auto()
    MOUNT_SURVEYOR_III = auto()
    MOUNT_SENSOR_ARRAY_I = auto()
    MOUNT_SENSOR_ARRAY_II = auto()
    MOUNT_SENSOR_ARRAY_III = auto()
    MOUNT_MINING_LASER_I = auto()
    MOUNT_MINING_LASER_II = auto()
    MOUNT_MINING_LASER_III = auto()
    MOUNT_LASER_CANNON_I = auto()
    MOUNT_MISSILE_LAUNCHER_I = auto()
    MOUNT_TURRET_I = auto()


class ShipNavFlightMode(SymbolEnums):
    DRIFT = auto()
    STEALTH = auto()
    CRUISE = auto()
    BURN = auto()


class ShipNavStatus(SymbolEnums):
    IN_TRANSIT = auto()
    IN_ORBIT = auto()
    DOCKED = auto()


class ShipReactorType(SymbolEnums):
    REACTOR_SOLAR_I = auto()
    REACTOR_FUSION_I = auto()
    REACTOR_FISSION_I = auto()
    REACTOR_CHEMICAL_I = auto()
    REACTOR_ANTIMATTER_I = auto()


class ShipRole(SymbolEnums):
    FABRICATOR = auto()
    HARVESTER = auto()
    HAULER = auto()
    INTERCEPTOR = auto()
    EXCAVATOR = auto()
    TRANSPORT = auto()
    REPAIR = auto()
    SURVEYOR = auto()
    COMMAND = auto()
    CARRIER = auto()
    PATROL = auto()
    SATELLITE = auto()
    EXPLORER = auto()
    REFINERY = auto()


class SystemType(SymbolEnums):
    NEUTRON_STAR = auto()
    RED_STAR = auto()
    ORANGE_STAR = auto()
    BLUE_STAR = auto()
    YOUNG_STAR = auto()
    WHITE_DWARF = auto()
    BLACK_HOLE = auto()
    HYPERGIANT = auto()
    NEBULA = auto()
    UNSTABLE = auto()


class TradeGoodsSymbols(SymbolEnums):
    PRECIOUS_STONES = auto()
    QUARTZ_SAND = auto()
    SILICON_CRYSTALS = auto()
    AMMONIA_ICE = auto()
    LIQUID_HYDROGEN = auto()
    LIQUID_NITROGEN = auto()
    ICE_WATER = auto()
    EXOTIC_MATTER = auto()
    ADVANCED_CIRCUITRY = auto()
    GRAVITON_EMITTERS = auto()
    IRON = auto()
    IRON_ORE = auto()
    COPPER = auto()
    COPPER_ORE = auto()
    ALUMINUM = auto()
    ALUMINUM_ORE = auto()
    SILVER = auto()
    SILVER_ORE = auto()
    GOLD = auto()
    GOLD_ORE = auto()
    PLATINUM = auto()
    PLATINUM_ORE = auto()
    DIAMONDS = auto()
    URANITE = auto()
    URANITE_ORE = auto()
    MERITIUM = auto()
    MERITIUM_ORE = auto()
    HYDROCARBON = auto()
    ANTIMATTER = auto()
    FERTILIZERS = auto()
    FABRICS = auto()
    FOOD = auto()
    JEWELRY = auto()
    MACHINERY = auto()
    FIREARMS = auto()
    ASSAULT_RIFLES = auto()
    MILITARY_EQUIPMENT = auto()
    EXPLOSIVES = auto()
    LAB_INSTRUMENTS = auto()
    AMMUNITION = auto()
    ELECTRONICS = auto()
    SHIP_PLATING = auto()
    EQUIPMENT = auto()
    FUEL = auto()
    MEDICINE = auto()
    DRUGS = auto()
    CLOTHING = auto()
    MICROPROCESSORS = auto()
    PLASTICS = auto()
    POLYNUCLEOTIDES = auto()
    BIOCOMPOSITES = auto()
    NANOBOTS = auto()
    AI_MAINFRAMES = auto()
    QUANTUM_DRIVES = auto()
    ROBOTIC_DRONES = auto()
    CYBER_IMPLANTS = auto()
    GENE_THERAPEUTICS = auto()
    NEURAL_CHIPS = auto()
    MOOD_REGULATORS = auto()
    VIRAL_AGENTS = auto()
    MICRO_FUSION_GENERATORS = auto()
    SUPERGRAINS = auto()
    LASER_RIFLES = auto()
    HOLOGRAPHICS = auto()
    SHIP_SALVAGE = auto()
    RELIC_TECH = auto()
    NOVEL_LIFEFORMS = auto()
    BOTANICAL_SPECIMENS = auto()
    CULTURAL_ARTIFACTS = auto()
    REACTOR_SOLAR_I = auto()
    REACTOR_FUSION_I = auto()
    REACTOR_FISSION_I = auto()
    REACTOR_CHEMICAL_I = auto()
    REACTOR_ANTIMATTER_I = auto()
    ENGINE_IMPULSE_DRIVE_I = auto()
    ENGINE_ION_DRIVE_I = auto()
    ENGINE_ION_DRIVE_II = auto()
    ENGINE_HYPER_DRIVE_I = auto()
    MODULE_MINERAL_PROCESSOR_I = auto()
    MODULE_CARGO_HOLD_I = auto()
    MODULE_CREW_QUARTERS_I = auto()
    MODULE_ENVOY_QUARTERS_I = auto()
    MODULE_PASSENGER_CABIN_I = auto()
    MODULE_MICRO_REFINERY_I = auto()
    MODULE_ORE_REFINERY_I = auto()
    MODULE_FUEL_REFINERY_I = auto()
    MODULE_SCIENCE_LAB_I = auto()
    MODULE_JUMP_DRIVE_I = auto()
    MODULE_JUMP_DRIVE_II = auto()
    MODULE_JUMP_DRIVE_III = auto()
    MODULE_WARP_DRIVE_I = auto()
    MODULE_WARP_DRIVE_II = auto()
    MODULE_WARP_DRIVE_III = auto()
    MODULE_SHIELD_GENERATOR_I = auto()
    MODULE_SHIELD_GENERATOR_II = auto()
    MOUNT_GAS_SIPHON_I = auto()
    MOUNT_GAS_SIPHON_II = auto()
    MOUNT_GAS_SIPHON_III = auto()
    MOUNT_SURVEYOR_I = auto()
    MOUNT_SURVEYOR_II = auto()
    MOUNT_SURVEYOR_III = auto()
    MOUNT_SENSOR_ARRAY_I = auto()
    MOUNT_SENSOR_ARRAY_II = auto()
    MOUNT_SENSOR_ARRAY_III = auto()
    MOUNT_MINING_LASER_I = auto()
    MOUNT_MINING_LASER_II = auto()
    MOUNT_MINING_LASER_III = auto()
    MOUNT_LASER_CANNON_I = auto()
    MOUNT_MISSILE_LAUNCHER_I = auto()
    MOUNT_TURRET_I = auto()


class TransactionType(SymbolEnums):
    PURCHASE = auto()
    SELL = auto()


class WaypointType(SymbolEnums):
    PLANET = auto()
    GAS_GIANT = auto()
    MOON = auto()
    ORBITAL_STATION = auto()
    JUMP_GATE = auto()
    ASTEROID_FIELD = auto()
    NEBULA = auto()
    DEBRIS_FIELD = auto()
    GRAVITY_WELL = auto()


class Agent(ApiModel):
    account_id: str = Field(min_length=1) 
    symbol: str = Field(min_length=3, max_length=14)
    headquarters: str
    credits: int
    starting_faction: str = Field(min_length=1)
    ship_count: int


class Chart(ApiModel):
    waypoint_symbol: str
    submitted_by: str
    submitted_on: datetime


class ConnectedSystem(ApiModel):
    symbol: str = Field(min_length=1)
    sector_symbol: str = Field(min_length=1)
    type: SystemType
    faction_symbol: FactionSymbols
    x: int
    y: int
    distance: int


class Contract(ApiModel):
    id = constr(min_length=1)
    faction_symbol: FactionSymbols
    type: ContractType
    terms: ContractTerms
    accepted: bool = False
    fulfilled: bool = False
    expiration: datetime | None
    deadline_to_accept: datetime | None


class ContractDeliverGood(ApiModel):
    trade_symbol: TradeGoodsSymbols
    destination_symbol = constr(min_length=1)
    units_required: int
    units_fulfilled: int


class ContractPayment(ApiModel):
    on_accepted: int
    on_fulfilled: int


class ContractTerms(ApiModel):
    deadline: datetime
    payment: ContractPayment
    deliver: list[ContractDeliverGood]


class Cooldown(ApiModel):
    ship_symbol = constr(min_length=1)
    total_seconds = conint(ge=0)
    remaining_seconds = conint(ge=0)
    expiration: datetime


class Extraction(ApiModel):
    ship_symbol = constr(min_length=1)
    yield_: ExtractionYield


class ExtractionYield(ApiModel):
    symbol: TradeGoodsSymbols
    units: int


class Faction(ApiModel):
    symbol: FactionSymbols
    name = constr(min_length=1)
    description = constr(min_length=1)
    headquarters = constr(min_length=1)
    traits: list[FactionTrait]
    is_recruiting: bool


class FactionTrait(ApiModel):
    symbol: FactionTraitSymbols
    name: str
    description: str


class JumpGate(ApiModel):
    jump_range: int
    faction_symbol: FactionSymbols
    connected_systems: list[System]


class Market(ApiModel):
    symbol: str
    exports: list[TradeGood]
    imports: list[TradeGood]
    exchange: list[TradeGood]
    transactions: list[MarketTransaction]
    trade_goods: list[MarketTradeGood]


class MarketTradeGood(ApiModel):
    symbol: TradeGoodsSymbols
    trade_volume = conint(ge=1)
    supply: MarketSupply
    purchase_price = conint(ge=0)
    sell_price = conint(ge=0)


class MarketTransaction(ApiModel):
    waypoint_symbol: str
    ship_symbol: str
    trade_symbol: TradeGoodsSymbols
    type_: Literal["PURCHASE"] | Literal["SELL"]
    units = conint(ge=0)
    price_perUnit = conint(ge=0)
    total_price = conint(ge=0)
    timestamp: datetime


class Meta(ApiModel):
    total = conint(ge=0)
    page: conint(ge=1) = 1  # type: ignore
    limit: conint(ge=1, le=20) = 10  # type: ignore


class ScannedShip(ApiModel):
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    frame: dict[str, ShipFrameType]
    reactor: dict[str, ShipReactorType]
    engine: dict[str, ShipEngineType]
    mounts: dict[str, ShipMountType]
    

class ScannedSystem(ApiModel):
    symbol = constr(min_length=1)
    sector_symbol = constr(min_length=1)
    type: SystemType
    x: int
    y: int
    distance: int


class ScannedWaypoint(ApiModel):
    symbol = constr(min_length=1)
    type: WaypointType
    system_symbol = constr(min_length=1)
    x: int
    y: int
    orbitals: list[Waypoint]
    faction: FactionSymbols
    traits: list[WaypointTrait]
    chart: Chart


class Ship(ApiModel):
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    crew: ShipCrew
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    cooldown: Cooldown
    modules: list[ShipModule]
    mounts: list[ShipMount]
    cargo: ShipCargo
    fuel: ShipFuel


class ShipCargo(ApiModel):
    capacity = conint(ge=0)
    units = conint(ge=0)
    inventory: list[ShipCargoItem]


class ShipCargoItem(ApiModel):
    symbol: str
    name: str
    description: str
    units = conint(ge=1)


class ShipCondition(ApiModel):
    value: conint(ge=0, le=100) # type: ignore


class ShipCrew(ApiModel):
    current: int
    required: int
    capacity: int
    rotation: Literal["STRICT"] | Literal["RELAXED"] = "STRICT"
    morale = conint(ge=0, le=100)
    wages = conint(ge=0)


class ShipEngine(ApiModel):
    symbol: ShipEngineType
    name: str
    description: str
    condition: ShipCondition
    speed: conint(ge=1)
    requirements: ShipRequirements


class ShipFrame(ApiModel):
    symbol: ShipFrameType
    name: str
    description: str
    condition: ShipCondition
    module_slots: conint(ge=0)
    mounting_points: conint(ge=0)
    fuel_capacity: conint(ge=0)
    requirements: ShipRequirements


class ShipFuel(ApiModel):
    current: conint(ge=0)
    capacity: conint(ge=0)
    consumed: ShipFuelConsumed


class ShipFuelConsumed(ApiModel):
    amount: conint(ge=0)
    timestamp: datetime


class ShipModificationTransaction(ApiModel):
    waypoint_symbol: str
    ship_symbol: str
    trade_symbol: TradeGoodsSymbols
    total_price: conint(ge=0)
    timestamp: datetime


class ShipModule(ApiModel):
    symbol: ShipModuleType
    capacity: int
    range: int
    name: str
    description: str
    requirements: ShipRequirements


class ShipMount(ApiModel):
    symbol: ShipMountType
    name: str
    description: str
    strength: conint(ge=0) # type: ignore
    deposits: list[DepositType]
    requirements: ShipRequirements


class ShipNav(ApiModel):
    system_symbol: str
    waypoint_symbol: str
    route: ShipNavRoute
    status: ShipNavStatus
    flight_mode: ShipNavFlightMode = ShipNavFlightMode.CRUISE


class ShipNavRoute(ApiModel):
    destination: ShipNavRouteWaypoint
    departure: ShipNavRouteWaypoint
    departure_time: datetime
    arrival: datetime


class ShipNavRouteWaypoint(ApiModel):
    symbol: str
    type: WaypointType
    system_symbol: str
    x: int
    y: int


class ShipReactor(ApiModel):
    symbol: ShipReactorType
    name: str
    description: str
    condition: conint(ge=0, le=100) # type: ignore
    power_outage: conint(ge=1) # type: ignore
    requirements: ShipRequirements


class ShipRegistration(ApiModel):
    name: str
    faction_symbol: str
    role: ShipRole


class ShipRequirements(ApiModel):
    power: int
    crew: int
    slots: int


class ShipYard(ApiModel):
    symbol: str
    ship_types: list[dict[str, ShipType]]
    transactions: list[ShipyardTransaction]
    ships: list[Ship]





class TradeGood:
    symbol: TradeGoodsSymbols
    name: str
    description: str
